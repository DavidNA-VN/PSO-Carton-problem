# 📦 PSO Optimization for Carton Box Design  
Dùng thuật toán Particle Swarm Optimization (PSO) để tối ưu kích thước thùng carton dựa trên thể tích yêu cầu đầu vào.

---

## ⭐ 1. Giới thiệu

Trong nhiều bài toán thiết kế bao bì, ta cần tính toán kích thước tối ưu của một thùng carton hình hộp chữ nhật sao cho:

- **Đúng thể tích yêu cầu** (ví dụ: 500 ml, 1 lít, 2 lít, 10 lít…)
- **Diện tích bề mặt nhỏ nhất**, nhằm giảm chi phí vật liệu.

Gọi các kích thước:

- `L`: chiều dài  
- `W`: chiều rộng  
- `H`: chiều cao  

Ràng buộc:  
\[
L \cdot W \cdot H = V
\]

Diện tích bề mặt thùng:  
\[
S = 2(LW + LH + WH)
\]

🟩 **Mục tiêu**:  
Tìm `(L, W, H)` sao cho thùng vừa thể tích `V` và diện tích bề mặt `S` nhỏ nhất.

---

## ⭐ 2. Tại sao dùng PSO?

PSO phù hợp vì:

- Bài toán **phi tuyến**, khó tối ưu bằng đạo hàm.
- Không gian nghiệm **liên tục** và dễ mã hóa.
- PSO hội tụ nhanh, dễ triển khai.
- Dễ ứng dụng cho bất kỳ thể tích đầu vào nào.

Với bài toán này, PSO cho kết quả **rất chính xác** và thậm chí trùng với nghiệm tối ưu giải tích (hộp lập phương).

---

## ⭐ 3. Ý tưởng giải quyết

Ta tối ưu **hai biến**:  
\[
x = (L, W)
\]

Còn chiều cao:
\[
H = \frac{V}{L \cdot W}
\]

Hàm mục tiêu:
\[
f(L, W) = 2(LW + L\frac{V}{LW} + W\frac{V}{LW})
\]

PSO sẽ cập nhật các giá trị `(L, W)` để giảm dần diện tích `S`.

---

## ⭐ 4. Cách chạy chương trình

### ✔ Yêu cầu
- Python 3.8+
- `numpy`

Cài đặt numpy:

```bash
pip install numpy
