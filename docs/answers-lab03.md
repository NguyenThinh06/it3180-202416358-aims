# Câu hỏi thảo luận Lab 03 – Quản lý cấu hình phần mềm (IT3180)

## Câu 1: Merge base là gì? Vai trò của nó khi Git thực hiện merge 3 chiều (3-way merge)?
- **Khái niệm:** **Merge base** là tổ tiên chung gần nhất (Nearest Common Ancestor) của hai nhánh đang được gộp vào nhau trên đồ thị lịch sử commit (có thể tìm bằng lệnh `git merge-base <nhánh-A> <nhánh-B>`).
- **Vai trò trong 3-way merge:**
  - Nếu chỉ so sánh trực tiếp 2 đầu nhánh A và B (2-way), Git chỉ thấy một dòng mã khác nhau nhưng không biết nhánh nào vừa sửa đổi và nhánh nào giữ nguyên bản gốc.
  - Khi đối chiếu cả hai nhánh với **Merge base**:
    - Nếu dòng mã chỉ thay đổi ở một nhánh so với Merge base (nhánh kia giữ nguyên), Git tự động áp dụng phần thay đổi đó.
    - Nếu cả hai nhánh cùng sửa đổi một dòng theo hai cách khác nhau so với Merge base, Git sẽ phát hiện và báo **Merge Conflict** để lập trình viên giải quyết.

## Câu 2: Vì sao trên nhánh `master` và `release/*` bắt buộc phải dùng `git revert` thay vì `git reset` khi muốn hoàn tác?
- **Bảo toàn lịch sử chung (Shared History):** `master` và `release/*` là các nhánh dùng chung đã đẩy lên remote. `git reset` xóa bỏ commit bằng cách lùi con trỏ nhánh về quá khứ (viết lại lịch sử) và đòi hỏi `git push --force` (bị chặn bởi Branch Protection). Việc viết lại lịch sử nhánh chung sẽ làm lệch pha lịch sử trên máy của các thành viên khác.
- **Đảm bảo tính kiểm toán và truy vết (Auditability & Traceability):** `git revert` tạo ra một **commit mới** đảo ngược thay đổi của commit cũ mà không xóa lịch sử. Thay đổi hoàn tác này đi qua đúng quy trình Pull Request/Review, đồng thời lưu lại đầy đủ dấu vết trên lịch sử kho chứa về việc lỗi xuất hiện khi nào và được hoàn tác ở PR nào.