# Câu hỏi thảo luận Lab 01 – Quản lý cấu hình phần mềm (IT3180)

## Câu 1: Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ:**
  - `--global`: Được lưu ở thư mục người dùng hiện tại trên hệ điều hành, cụ thể là tệp `~/.gitconfig` (hoặc `~/.config/git/config`).
  - `--local`: Được lưu trực tiếp bên trong kho chứa (repository) hiện tại ở tệp `.git/config`.
- **Sự khác nhau:**
  - **Phạm vi tác dụng:** Cấu hình `--global` áp dụng mặc định cho **mọi repository** của người dùng đó trên máy tính. Trong khi đó, `--local` chỉ áp dụng riêng cho **repository hiện tại**.
  - **Độ ưu tiên:** Cấu hình `--local` có độ ưu tiên cao hơn và sẽ ghi đè (override) cấu hình `--global` nếu cả hai cùng thiết lập một thuộc tính (ví dụ: dùng email cá nhân ở `--global`, nhưng dùng email trường học `@sis.hust.edu.vn` ở `--local` cho dự án môn học).

## Câu 2: Vì sao dùng `git mv` thay vì xóa và tạo lại tệp (hoặc di chuyển bằng File Explorer)?
- **Ghi nhận trực tiếp vào Staging Area:** Lệnh `git mv <nguồn> <đích>` thực hiện đồng thời việc di chuyển tệp trên ổ cứng và cập nhật ngay sự thay đổi đó vào vùng Staging (Index) chỉ với một câu lệnh, thay vì phải tự di chuyển tệp rồi chạy `git rm` cho đường dẫn cũ và `git add` cho đường dẫn mới.
- **Bảo toàn lịch sử truy vết (History Tracking):** Khi dùng `git mv`, Git nhận diện rõ thao tác đổi tên/di chuyển (`renamed: cart.py -> aims/cart.py`) trên cùng một Configuration Item thay vì hiểu nhầm là xóa hẳn tệp cũ và thêm một tệp mới hoàn toàn. Nhờ đó, ta dễ dàng truy vết lịch sử xuyên suốt quá trình đổi tên bằng lệnh `git log --follow -- aims/cart.py`.

## Câu 3: `release/lab01` có phải là một baseline không? Vì sao?
- **Có.** Nhánh `release/lab01` chính là một **Baseline** (cơ sở cấu hình) của dự án tại thời điểm kết thúc Lab 01.
- **Giải thích theo lý thuyết SCM:**
  - Baseline là một phiên bản của các Configuration Item đã được hoàn thiện, kiểm tra (chạy `python main.py` ra kết quả chuẩn `Total cost: 63.89 $`) và đóng băng để làm mốc bàn giao/nộp bài.
  - Mọi thay đổi tiếp theo ở các bài Lab sau sẽ diễn ra trên `master` và các nhánh tính năng mới, không được phép tự ý sửa đổi trực tiếp lên `release/lab01` (nếu phát hiện lỗi trên bản đã nộp, bắt buộc phải đi qua quy trình kiểm soát thay đổi bằng nhánh `hotfix/*` và Pull Request).

## Câu 4: Vì sao không commit thẳng lên `master` dù chỉ làm việc một mình?
- **Đảm bảo nguyên tắc kiểm soát thay đổi (Change Control):** Trong SCM, nhánh `master` đóng vai trò là nhánh tích hợp chính luôn ở trạng thái ổn định. Việc tách nhánh riêng (`refactor/*`, `feature/*`, `topic/*`) giúp cô lập các thay đổi đang làm dở, tránh làm hỏng mã nguồn ổn định trên `master`.
- **Tạo điểm kiểm tra và đánh giá (Review & CI):** Đưa thay đổi qua Pull Request (PR) tạo ra một bước dừng bắt buộc để tự rà soát lại toàn bộ `Files changed` (kiểm tra xem có lọt tệp rác như `__pycache__` hay sót dòng `import` nào không) và kích hoạt kiểm thử tự động (CI) trước khi tích hợp.
- **Lưu vết ngữ cảnh rõ ràng (Traceability):** Mỗi PR gom nhóm các commit cùng phục vụ một mục đích duy nhất, có mô tả đầy đủ (Mục đích, Thay đổi, Cách kiểm thử), giúp việc kiểm toán lịch sử hoặc hoàn tác (`git revert`) cả một cụm thay đổi về sau trở nên an toàn và minh bạch.