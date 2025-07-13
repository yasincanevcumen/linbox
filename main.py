# Gerekli kütüphaneleri import ediyoruz
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)
CORS(app)

# Ana sayfayı ('/') servis eden kural
@app.route('/')
def index():
    return render_template('index.html')

# Hesaplama isteklerini yöneten kural
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        operation = data.get('operation')
        matrix_a_data = data.get('matrix')
        matrix_a = np.array(matrix_a_data)
        
        response_data = {}

        # Tek matrisli işlemler
        if operation in ['determinant', 'trace']:
            if matrix_a.shape[0] != matrix_a.shape[1]:
                raise ValueError("Bu işlem sadece kare matrisler için geçerlidir.")
            
            if operation == 'determinant':
                value = np.linalg.det(matrix_a)
                response_data = {"type": "scalar", "title": "Determinant", "data": f"{value:.4f}"}
            elif operation == 'trace':
                value = np.trace(matrix_a)
                response_data = {"type": "scalar", "title": "İz (Trace)", "data": f"{value:.4f}"}

        elif operation == 'eigenvalue':
            if matrix_a.shape[0] != matrix_a.shape[1]:
                raise ValueError("Özdeğerler sadece kare matrisler için hesaplanır.")
            values = np.linalg.eigvals(matrix_a)
            real_values = np.real_if_close(values).tolist()
            response_data = {"type": "eigenvalue", "title": "Özdeğerler (Eigenvalues)", "data": real_values}

        elif operation == 'transpose':
            matrix = matrix_a.T.tolist()
            response_data = {"type": "matrix", "title": "Transpoze", "data": matrix}

        elif operation == 'inverse':
            if matrix_a.shape[0] != matrix_a.shape[1] or np.linalg.det(matrix_a) == 0:
                raise ValueError("Ters matris için, matris kare olmalı ve determinantı sıfırdan farklı olmalıdır.")
            matrix = np.linalg.inv(matrix_a).tolist()
            response_data = {"type": "matrix", "title": "Ters Matris", "data": matrix}
        
        # İki matrisli işlemler
        elif operation in ['add', 'subtract', 'multiply']:
            matrix_b_data = data.get('matrixB')
            if not matrix_b_data:
                return jsonify({'error': 'Bu işlem için ikinci bir matris gerekli.'}), 400
            matrix_b = np.array(matrix_b_data)

            if operation == 'add':
                if matrix_a.shape != matrix_b.shape:
                    raise ValueError("Toplama için matris boyutları aynı olmalıdır.")
                matrix = np.add(matrix_a, matrix_b).tolist()
                response_data = {"type": "matrix", "title": "Toplama Sonucu", "data": matrix}
            elif operation == 'subtract':
                if matrix_a.shape != matrix_b.shape:
                    raise ValueError("Çıkarma için matris boyutları aynı olmalıdır.")
                matrix = np.subtract(matrix_a, matrix_b).tolist()
                response_data = {"type": "matrix", "title": "Çıkarma Sonucu", "data": matrix}
            elif operation == 'multiply':
                if matrix_a.shape[1] != matrix_b.shape[0]:
                    raise ValueError("Çarpma için ilk matrisin sütun sayısı, ikinci matrisin satır sayısına eşit olmalıdır.")
                matrix = np.matmul(matrix_a, matrix_b).tolist()
                response_data = {"type": "matrix", "title": "Çarpma Sonucu", "data": matrix}
        
        else:
            return jsonify({'error': 'Geçersiz işlem.'}), 400

        # Yapılandırılmış JSON verisini gönder
        return jsonify(response_data)

    except Exception as e:
        # Hata durumunda da yapılandırılmış bir hata mesajı gönder
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
