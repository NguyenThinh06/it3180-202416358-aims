# Câu hỏi thảo luận Lab 02 – Quản lý cấu hình phần mềm (IT3180)

## Câu 1: Vì sao phải đồng bộ `master` vào nhánh tính năng trước khi gửi/merge PR?
- **Phát hiện và giải quyết xung đột (Conflict) tại máy cá nhân:** Trong khi ta đang phát triển tính năng, nhánh `master` có thể đã nhận thêm các thay đổi mới từ đồng đội. Việc kéo `origin/master` về nhánh tính năng giúp lập trình viên tự giải quyết xung đột trên môi trường local thay vì đẩy gánh nặng cho người review.
- **Đảm bảo tính tích hợp (Integration Verification):** Đôi khi không có xung đột về mặt văn bản (Git merge tự động thành công), nhưng lại xung đột về mặt logic (ví dụ: hàm dùng chung bị đổi chữ ký hoặc thay đổi hành vi). Đồng bộ `master` về trước giúp ta chạy lại chương trình (`python main.py`) và bộ kiểm thử để chắc chắn tính năng mới hoạt động đúng khi ghép với mã nguồn mới nhất của `master`.

## Câu 2: Khi nào không được dùng `git rebase`?
- **Nguyên tắc vàng của Rebase:** Tuyệt đối **không rebase các nhánh công khai (public/shared branches)** như `master`, `release/*`, hoặc một nhánh tính năng đang có nhiều người cùng làm việc và đã push lên remote.
- **Lý do:** Lệnh `rebase` viết lại lịch sử bằng cách tạo ra các commit mới với mã băm (SHA) hoàn toàn mới thay thế cho các commit cũ. Nếu rebase một nhánh đã chia sẻ cho người khác, lịch sử trên máy của đồng đội sẽ bị lệch hoàn toàn với remote, dẫn đến việc khi họ `git pull` và `git push` lại sẽ tạo ra các commit trùng lặp và gây hỗn loạn lịch sử kho chứa. Rebase chỉ dùng cho các commit cục bộ hoặc nhánh cá nhân của riêng một người trước khi tích hợp.

## Câu 3: Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- **Nhánh `feature/*`:** Dùng để phát triển các **tính năng nghiệp vụ mới** của sản phẩm có tác động trực tiếp đến hành vi/chức năng phần mềm đối với người dùng cuối (ví dụ: `feature/cart-print`, `feature/search-by-title`). Các commit trên nhánh này thường mang tiền tố `feat:`.
- **Nhánh `topic/*`:** Dùng cho các **công việc kỹ thuật, tài liệu, cấu hình quy trình hoặc thử nghiệm** không trực tiếp thêm tính năng nghiệp vụ vào mã nguồn sản phẩm (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/prepare-release-1.0.0`, `topic/ci-unit-tests`). Các commit trên nhánh này thường mang tiền tố `docs:`, `chore:`, hoặc `ci:`.