# Gerekli kütüphaneleri import ediyoruz
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import numpy as np
import sympy # Sembolik matematik için eklendi

# Flask uygulamasını başlatıyoruz
app = Flask(__name__)
CORS(app)

# Ana sayfayı ('/') servis eden kural
@app.route('/')
def index():
    return render_template('index.html')

# Tüm hesaplama isteklerini yöneten ana kural
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        operation = data.get('operation')
        response_data = {}

        # --- MATRİS İŞLEMLERİ ---
        if operation in ["determinant", "transpose", "inverse", "trace", "eigenvalue", "add", "subtract", "multiply"]:
            matrix_a_data = data.get('matrix')
            if not matrix_a_data:
                return jsonify({'error': 'Matris verisi eksik.'}), 400
            matrix_a = np.array(matrix_a_data)

            if operation in ['determinant', 'trace']:
                if matrix_a.shape[0] != matrix_a.shape[1]: raise ValueError("Bu işlem sadece kare matrisler için geçerlidir.")
                value = np.linalg.det(matrix_a) if operation == 'determinant' else np.trace(matrix_a)
                response_data = {"type": "scalar", "title": operation.capitalize(), "data": f"{value:.4f}"}
            
            elif operation == 'eigenvalue':
                if matrix_a.shape[0] != matrix_a.shape[1]: raise ValueError("Özdeğerler sadece kare matrisler için hesaplanır.")
                values = np.linalg.eigvals(matrix_a)
                response_data = {"type": "eigenvalue", "title": "Özdeğerler", "data": np.real_if_close(values).tolist()}
            
            elif operation == 'transpose':
                response_data = {"type": "matrix", "title": "Transpoze", "data": matrix_a.T.tolist()}
            
            elif operation == 'inverse':
                if matrix_a.shape[0] != matrix_a.shape[1] or np.linalg.det(matrix_a) == 0: raise ValueError("Ters matris için, matris kare olmalı ve determinantı sıfırdan farklı olmalıdır.")
                response_data = {"type": "matrix", "title": "Ters Matris", "data": np.linalg.inv(matrix_a).tolist()}
            
            elif operation in ['add', 'subtract', 'multiply']:
                matrix_b_data = data.get('matrixB')
                if not matrix_b_data: return jsonify({'error': 'Bu işlem için ikinci bir matris gerekli.'}), 400
                matrix_b = np.array(matrix_b_data)
                
                if operation == 'add':
                    if matrix_a.shape != matrix_b.shape: raise ValueError("Toplama için boyutlar aynı olmalıdır.")
                    result_matrix = np.add(matrix_a, matrix_b)
                    title = "Toplama Sonucu"
                elif operation == 'subtract':
                    if matrix_a.shape != matrix_b.shape: raise ValueError("Çıkarma için boyutlar aynı olmalıdır.")
                    result_matrix = np.subtract(matrix_a, matrix_b)
                    title = "Çıkarma Sonucu"
                elif operation == 'multiply':
                    if matrix_a.shape[1] != matrix_b.shape[0]: raise ValueError("Çarpma için A'nın sütunları B'nin satırlarına eşit olmalıdır.")
                    result_matrix = np.matmul(matrix_a, matrix_b)
                    title = "Çarpma Sonucu"
                response_data = {"type": "matrix", "title": title, "data": result_matrix.tolist()}
        
        # --- KALKÜLÜS İŞLEMLERİ ---
        elif operation in ["derivative", "integral"]:
            function_str = data.get('function')
            if not function_str:
                return jsonify({'error': 'Fonksiyon girdisi eksik.'}), 400
            
            x = sympy.symbols('x')
            expr = sympy.sympify(function_str.replace('^', '**'), locals={'x': x})

            if operation == "derivative":
                derivative_expr = sympy.diff(expr, x)
                response_data = {
                    "type": "calculus", 
                    "title": f"f(x) = {expr} fonksiyonunun türevi", 
                    "data": str(derivative_expr).replace('**', '^')
                }
            
            elif operation == "integral":
                lower_bound_str = data.get('lower_bound')
                upper_bound_str = data.get('upper_bound')
                
                try:
                    lower_bound = sympy.sympify(lower_bound_str)
                    upper_bound = sympy.sympify(upper_bound_str)
                except (sympy.SympifyError, TypeError):
                    return jsonify({'error': 'İntegral sınırları sayısal veya sembolik (örn: pi) olmalıdır.'}), 400

                integral_val = sympy.integrate(expr, (x, lower_bound, upper_bound))
                
                # Sonucun sayısal olup olmadığını kontrol et
                if integral_val.is_number:
                    # Sonucu 4 ondalık basamağa yuvarla
                    result_str = f"{integral_val.evalf(4):.4f}"
                else:
                    result_str = str(integral_val).replace('**', '^')
                    
                response_data = {
                    "type": "calculus", 
                    "title": f"f(x) = {expr} fonksiyonunun [{lower_bound}, {upper_bound}] aralığındaki integrali", 
                    "data": result_str
                }
        else:
            return jsonify({'error': 'Geçersiz işlem talebi.'}), 400

        return jsonify(response_data)

    except (sympy.SympifyError, SyntaxError):
        return jsonify({'error': 'Geçersiz fonksiyon formatı. Lütfen ifadeyi kontrol edin (örn: x**2 + 2*x).'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
