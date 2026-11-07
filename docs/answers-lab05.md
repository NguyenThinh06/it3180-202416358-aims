# Câu hỏi thảo luận Lab 05 – Quản lý cấu hình phần mềm (IT3180)

## Câu 1: Vì sao ở Phần A khi mới tạo `release/lab05` ta chưa gắn ngay tag `v1.1.0`?
- **Tag là mốc bất biến (Immutable):** Một khi đã gắn tag `v1.1.0` và đẩy lên remote (`git push origin v1.1.0`), ta không được xóa hay dịch chuyển tag đó sang commit khác.
- Khi nhánh `release/lab05` đang trong giai đoạn chuẩn bị trước khi chính thức phát hành mà phát hiện lỗi từ bản cũ (`v1.0.0`) cần cherry-pick sang, việc chưa gắn tag giúp ta đưa bản vá vào `release/lab05` rồi mới đóng dấu `v1.1.0`. Nếu đã trót gắn tag `v1.1.0` từ Phần A, bản vá đưa vào sau bắt buộc phải phát hành thành phiên bản mới `v1.1.1`.

## Câu 2: Ưu, nhược điểm của "Upstream First" (sửa trên `master` trước rồi cherry-pick về `release/*`) so với "Release First" (sửa từ `release/*` rồi cherry-pick lên `master`)?
- **Upstream First (Microsoft Release Flow):**
  - *Ưu điểm:* Đảm bảo mọi lỗi luôn được giải quyết trên nhánh phát triển chính (`master`) trước, tránh lỗi tái xuất hiện (regression) ở bản phát hành tương lai do quên cherry-pick về `master`.
  - *Nhược điểm:* Mã nguồn trên `master` có thể đã thay đổi cấu trúc nhiều so với nhánh `release/*` cũ; khi backport ngược về `release/*` dễ gặp xung đột hoặc phụ thuộc vào mã chưa tồn tại ở bản cũ.
- **Release First (Mô hình trong học phần):**
  - *Ưu điểm:* Nhánh `hotfix/*` tách trực tiếp từ đúng baseline đang gặp lỗi (`release/lab04`), giúp tái hiện lỗi chính xác trên `v1.0.0`, kiểm thử cô lập và phát hành bản vá `v1.0.1` nhanh nhất mà không lẫn các tính năng đang làm dở trên `master`.
  - *Nhược điểm:* Đòi hỏi quy trình kiểm toán chặt chẽ để không quên lan truyền (`cherry-pick -x`) bản sửa lên `master` và các nhánh `release/*` khác.

## Câu 3: Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- **Lệnh `git log --all --oneline --grep="cherry picked from commit <FIX_SHA>"`:** Chỉ hiện 1 commit trên `master` thay vì 2 commit (thiếu bản trên `release/lab05`).
- **Lệnh `git cherry -v origin/release/lab05 origin/release/lab04`:** Sẽ in ra dấu `+ <FIX_SHA> fix: make search_by_title case-insensitive`, báo hiệu commit sửa lỗi đã có trên `release/lab04` nhưng chưa có bản tương đương trên `release/lab05`.
- **Vòng lặp kiểm tra hành vi trên 3 phiên bản (`v1.0.1`, `v1.1.0`, `master`):** Kết quả trên `v1.1.0` sẽ in ra `0` thay vì `1`.
