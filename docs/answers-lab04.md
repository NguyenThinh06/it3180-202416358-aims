# Câu hỏi thảo luận Lab 04 – Quản lý cấu hình phần mềm (IT3180)

## Câu 1: Vì sao phải chuẩn bị phát hành (cập nhật số phiên bản, viết CHANGELOG) trên `master` trước, mà không sửa trực tiếp trên nhánh `release/*`?
- **Tuân thủ nguyên tắc một chiều (One-way Release Branch):** Trong mô hình Release Flow của học phần, nhánh `release/*` không bao giờ được merge ngược lại vào `master`. Nếu sửa số phiên bản và viết `CHANGELOG.md` trực tiếp trên `release/lab04`, nhánh `master` sẽ bị thiếu các thông tin lịch sử phát hành đó ở các phiên bản tiếp theo.
- **Đảm bảo tính bất biến của Baseline:** Khi cắt nhánh `release/lab04` từ `master`, bản thân commit đầu nhánh đã hoàn chỉnh mọi thông tin định danh (`__version__ = "1.0.0"`, `CHANGELOG.md`) và sẵn sàng đóng băng ngay lập tức bằng tag `v1.0.0` mà không cần phát sinh thêm commit chỉnh sửa hậu kỳ.

## Câu 2: Vì sao nhánh `release/*` không bao giờ merge ngược vào `master`?
- **Tránh xung đột phiên bản và nhiễu lịch sử:** Nhánh `release/*` là dòng bảo trì riêng của một phiên bản đã phát hành (ví dụ dòng `1.0.x`), trong khi `master` đã tiến lên phát triển phiên bản mới (`1.1.0`). Nếu merge cả nhánh `release/*` vào `master`, các commit nâng số phiên bản cục bộ (như `1.0.1`) sẽ ghi đè và gây xung đột trực tiếp với cấu hình phiên bản trên `master`.
- **Kiểm soát chọn lọc bằng Cherry-pick:** Khi có bản vá lỗi (hotfix) trên nhánh `release/*`, ta chỉ truyền duy nhất commit sửa mã nguồn sang `master` bằng `git cherry-pick -x`, giữ cho hai dòng phát triển và bảo trì tách biệt, sạch sẽ.

## Câu 3: So sánh mô hình Release Flow (của học phần) với GitFlow truyền thống.
- **Số lượng nhánh dài hạn:** GitFlow duy trì 2 nhánh chính song song là `main` (chỉ chứa các bản release chính thức) và `develop` (nhánh tích hợp phát triển), cùng các nhánh phụ `feature/*`, `release/*`, `hotfix/*`. Trong khi đó, Release Flow rút gọn chỉ dùng **một nhánh tích hợp duy nhất là `master`**; mọi tính năng merge thẳng vào `master` và đến kỳ phát hành thì cắt nhánh `release/*` từ `master`.
- **Luồng kết thúc của nhánh `release/*`:** Trong GitFlow, nhánh `release/*` chỉ sống ngắn hạn để chuẩn bị phát hành rồi merge vào cả `main` lẫn `develop` và bị xóa đi. Ngược lại, trong Release Flow, nhánh `release/*` là nhánh sống dài hạn đóng vai trò dòng bảo trì cho phiên bản đó và không bao giờ merge ngược về `master`.

## Câu 4: Vì sao ở Lab 04 phiên bản được nâng lên `1.0.0` mà không phải là `0.4.0`?
- Theo chuẩn **Semantic Versioning (SemVer)**:
  - Các phiên bản `0.y.z` (`v0.1.0`, `v0.2.0`, `v0.3.0` ở Lab 01–03) dành cho giai đoạn phát triển ban đầu (initial development), khi cấu trúc gói và các tính năng cốt lõi vẫn đang thay đổi liên tục.
  - Phiên bản `1.0.0` đánh dấu mốc phần mềm đã hoàn thiện đầy đủ các chức năng cơ bản theo đặc tả (quản lý giỏ hàng, in giỏ hàng, tìm kiếm, tính giảm giá, có bộ unit test kiểm chứng) và chính thức phát hành bản ổn định đầu tiên (Public Baseline / First Stable Release) cho người dùng.