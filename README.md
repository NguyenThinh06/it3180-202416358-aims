# AIMS-mini — Báo cáo & Hướng dẫn Thực hành IT3180

Ứng dụng dòng lệnh Python mô phỏng hệ thống quản lý đĩa DVD cửa hàng AIMS. Đây là dự án thực hành học phần **Quản lý cấu hình phần mềm (IT3180)** (chuỗi Lab 01–05), áp dụng quy trình **Release Flow** với Git và GitHub để quản lý mã nguồn, nhánh, phiên bản, CI/CD và kiểm toán cấu hình.

- **Sinh viên:** Nguyễn Văn Thịnh — **MSSV:** 202416358
- **Repository:** [NguyenThinh06/it3180-202416358-aims](https://github.com/NguyenThinh06/it3180-202416358-aims) (public)
- **Phiên bản mã nguồn hiện tại:** `1.1.0`
- **Yêu cầu môi trường:** Python ≥ 3.10; chỉ sử dụng thư viện chuẩn (`unittest`)

---

## 📖 Mục lục

- [Hướng dẫn cài đặt và sử dụng](#hướng-dẫn-cài-đặt-và-sử-dụng)
- [Kiểm thử tự động](#kiểm-thử-tự-động)
- [Tài liệu thảo luận Lab 01–05](#tài-liệu-thảo-luận-lab-0105)
- [BÁO CÁO THỰC HÀNH — AIMS-MINI (IT3180)](#báo-cáo-thực-hành--aims-mini-it3180)
  - [1. Tổng quan](#1-tổng-quan)
  - [2. Nhánh nộp bài & Tag](#2-nhánh-nộp-bài--tag)
  - [3. Pull Request](#3-pull-request)
  - [4. Issue (Truy vết Issue ⇄ Nhánh ⇄ Commit ⇄ PR)](#4-issue-truy-vết-issue--nhánh--commit--pr)
  - [5. GitHub Actions (CI)](#5-github-actions-ci)
  - [6. Status Accounting & Kiểm toán cấu hình (Lab 04–05)](#6-status-accounting--kiểm-toán-cấu-hình-lab-0405)
  - [7. Việc đã làm & Bài học từ các sai sót thực tế](#7-việc-đã-làm--bài-học-từ-các-sai-sót-thực-tế)

---

## Hướng dẫn cài đặt và sử dụng

### 1. Clone kho mã nguồn

```bash
git clone https://github.com/NguyenThinh06/it3180-202416358-aims.git
cd it3180-202416358-aims
```

### 2. Chạy chương trình

```bash
python main.py
```
*(Trên Linux/macOS dùng `python3 main.py`)*

Kết quả chạy mẫu in thông tin giỏ hàng và tổng chi phí:
```text
AIMS-mini v1.1.0
Đã thêm đĩa vào giỏ hàng
Đã thêm đĩa vào giỏ hàng
Đã thêm đĩa vào giỏ hàng
***********************CART***********************
Ordered Items:
1. DVD - The Lion King - Animation - Roger Allers - 87: 19.95 $
2. DVD - Star Wars - Science Fiction - George Lucas - 87: 24.95 $
3. DVD - Aladdin - Animation -  - 0: 18.99 $
Total cost: 63.89 $
**************************************************
```

> [!NOTE]
> **Lưu ý encoding trên Windows PowerShell / CMD:**
> Mã nguồn sử dụng thông báo tiếng Việt `"Đã thêm đĩa vào giỏ hàng"`. Trên Windows có bảng mã console mặc định `cp1252`, nếu gặp lỗi hiển thị hãy bật chế độ UTF-8:
> ```powershell
> python -X utf8 main.py
> ```

---

## Kiểm thử tự động

Chạy bộ 8 bài kiểm thử đơn vị (`unittest`) từ thư mục gốc repository:

```bash
python -m unittest discover -s tests -v
```
*(Trên Windows PowerShell: `python -X utf8 -m unittest discover -s tests -v`)*

Kết quả kỳ vọng: **Ran 8 tests in 0.001s — OK**.

---

## Tài liệu thảo luận Lab 01–05

Các câu trả lời thảo luận lý thuyết SCM và phân tích thiết kế chi tiết nằm trong thư mục `docs/`:

| Lab | Chủ đề chính | Tệp tài liệu |
|---|---|---|
| **01** | Thiết lập môi trường, 3 vùng làm việc, `git mv`, baseline và quy trình nhánh | [answers-lab01.md](docs/answers-lab01.md) |
| **02** | Đồng bộ master, nguyên tắc cấm rebase, phân biệt `feature/*` và `topic/*` | [answers-lab02.md](docs/answers-lab02.md) |
| **03** | Bản chất 3-way merge, merge base, lý do bắt buộc `git revert` trên master/release | [answers-lab03.md](docs/answers-lab03.md) |
| **04** | Chuẩn bị phát hành, tính một chiều của release branch, so sánh GitFlow vs Release Flow, SemVer 1.0.0 | [answers-lab04.md](docs/answers-lab04.md) |
| **05** | Chính sách hotfix, thời điểm gắn tag release, so sánh Upstream First vs Release First | [answers-lab05.md](docs/answers-lab05.md) |

Tài liệu bổ sung: [use-case.md](docs/use-case.md) (Phân tích sơ đồ ca sử dụng hệ thống AIMS-mini).

---

# BÁO CÁO THỰC HÀNH — AIMS-MINI (IT3180)

**Sinh viên:** Nguyễn Văn Thịnh — **MSSV:** 202416358 · **Repository:** [it3180-202416358-aims](https://github.com/NguyenThinh06/it3180-202416358-aims) (public)

Tài liệu này tổng hợp bằng chứng cấu hình, lịch sử commit, Pull Request, Issue, kiểm thử CI/CD và kết quả kiểm toán cho toàn bộ chuỗi **Lab 01 – Lab 05** (Quản lý cấu hình phần mềm với Git & GitHub).

---

## 1. Tổng quan

| Hạng mục | Giá trị |
|---|---|
| **Nhánh mặc định** | `master` |
| **Số Pull Request** | **24** (đã merge: **24**, 100%) |
| **Số Issue** | **2** (đã đóng: **2**, đóng tự động qua từ khóa `Fixes #N`) |
| **Tag annotated** | `v0.1.0`, `v0.2.0`, `v0.3.0`, `v1.0.0`, `v1.0.1`, `v1.1.0` (Tổng: 6) |
| **GitHub Release** | `v1.0.0` (Baseline Lab 04) |
| **Số nhánh trên remote** | **7** (`master`, `release/lab01`, `release/lab02`, `release/lab03`, `release/lab04`, `release/lab05`, `topic/answers-lab03`) |
| **Kiểm thử trên master** | `Ran 8 tests in 0.001s - OK` |
| **CI** | GitHub Actions (`.github/workflows/ci.yml`), check `test` — bắt buộc vượt qua với master |
| **Branch protection** | Bật trên `master` và `release/*`: Bắt buộc Pull Request, không cho phép Force Push, không cho phép xóa nhánh |

### Thực nghiệm kiểm chứng Branch Protection (Checklist Lab 02 & Lab 04)
Thực hiện push trực tiếp một commit lên nhánh được bảo vệ:
```bash
$ git switch release/lab04
$ git commit --allow-empty -m "chore: test branch protection"
$ git push origin release/lab04
remote: error: GH006: Protected branch update failed for refs/heads/release/lab04.
remote: - Changes must be made through a pull request.
! [remote rejected] release/lab04 -> release/lab04 (protected branch hook declined)
error: failed to push some refs to 'github.com:NguyenThinh06/it3180-202416358-aims.git'
```
Sau kiểm chứng, nhánh được hoàn tác bằng `git reset --hard origin/release/lab04` để bảo toàn baseline.

---

## 2. Nhánh nộp bài & Tag

| Lab | Nhánh nộp bài | Tag | Tệp trả lời thảo luận |
|:---:|:---|:---:|:---|
| **01** | `release/lab01` | `v0.1.0` | `docs/answers-lab01.md` |
| **02** | `release/lab02` | `v0.2.0` | `docs/answers-lab02.md` |
| **03** | `release/lab03` | `v0.3.0` | `docs/answers-lab03.md` |
| **04** | `release/lab04` | `v1.0.0` (+ `v1.0.1` bản vá) | `docs/answers-lab04.md` |
| **05** | `release/lab05` | `v1.1.0` | `docs/answers-lab05.md` |

### Bằng chứng `git tag -n`:
```text
v0.1.0          Lab 01 release
v0.2.0          Lab 02 release
v0.3.0          Lab 03 release
v1.0.0          AIMS-mini 1.0.0 Lab 04 release
v1.0.1          AIMS-mini 1.0.1 - hotfix search_by_title
v1.1.0          AIMS-mini 1.1.0 Lab 05 release
```

---

## 3. Pull Request

Toàn bộ **24 Pull Request** được tạo và tích hợp thành công trên kho mã nguồn:

| PR | Nhánh nguồn → Base | Tiêu đề PR | Trạng thái | Merge Commit |
|:---:|:---|:---|:---:|:---:|
| **#1** | `refactor/apply-release-flow` → `master` | Refactor/apply release flow | MERGED | `ab5274d` |
| **#2** | `topic/answers-lab01` → `master` | docs: add discussion answers for lab 01 | MERGED | `d02d195` |
| **#3** | `topic/pr-template` → `master` | docs: add pull request template | MERGED | `8a11e54` |
| **#4** | `feature/cart-print` → `master` | feat: add cart printing functionality | MERGED | `309db5e` |
| **#5** | `feature/search-by-title` → `master` | Feature/search by title | MERGED | `a11fdc0` |
| **#6** | `topic/use-case-diagram` → `master` | docs: add use case diagram | MERGED | `32f017b` |
| **#7** | `topic/answers-lab02` → `master` | docs: add discussion answers for lab 02 | MERGED | `c033ecb` |
| **#9** | `bugfix/cart-limit-off-by-one` → `master` | Bugfix/cart limit off by one | MERGED | `69cac65` |
| **#10** | `bugfix/discount-calculation` → `feature/discount` | fix: return discounted total and validate percent | MERGED | `444c586` |
| **#11** | `feature/discount` → `master` | Feature/discount | MERGED | `37cdc78` |
| **#12** | `feature/vietnamese-messages` → `master` | feat: translate cart added message to Vietnamese | MERGED | `d74c90e` |
| **#13** | `feature/show-added-title` → `master` | Feature/show added title | MERGED | `f2b03fc` |
| **#14** | `bugfix/revert-show-added-title` → `master` | Revert "Merge pull request #13 from feature/show-added-title" | MERGED | `c8d9ad1` |
| **#15** | `topic/prepare-release-1.0.0` → `master` | chore: prepare release 1.0.0 | MERGED | `fe26f86` |
| **#16** | `feature/sort-cart` → `master` | feat: add sort_by_title and sort_by_cost to Cart | MERGED | `652c2f1` |
| **#17** | `topic/answers-lab04` → `master` | docs: add discussion answers for lab 03 and lab 04 | MERGED | `efa17e0` |
| **#18** | `feature/search-by-category` → `master` | feat: add search_by_category function | MERGED | `7126cb3` |
| **#19** | `topic/prepare-release-1.1.0` → `master` | chore: prepare release 1.1.0 | MERGED | `fffc964` |
| **#21** | `hotfix/search-case-insensitive` → `release/lab04` | Hotfix/search case insensitive | MERGED | `6c0f7c2` |
| **#22** | `hotfix/search-case-insensitive-master` → `master` | Hotfix/search case insensitive master | MERGED | `5b9551c` |
| **#23** | `hotfix/search-case-insensitive-lab05` → `release/lab05` | fix: make search_by_title case-insensitive | MERGED | `c61aefc` |
| **#24** | `fix/update-search-functions` → `master` | Fix/update search functions | MERGED | `f91fa81` |
| **#25** | `fix/search-release-lab05` → `release/lab05` | fix: ensure search_by_title exists in release/lab05 | MERGED | `f625be2` |
| **#26** | `topic/ci-unit-tests` → `master` | ci: add GitHub Actions workflow and lab 05 answers | MERGED | `b8e7bbb` |

### Thực nghiệm đủ 3 kiểu Merge trong Lab 02:
1. **Merge commit (PR #4):** Giữ nguyên toàn bộ 3 commit phát triển và vòng review (`67bff7f`, `11e4b7a`, `4949e1e`) tích hợp vào `master` tại commit merge `309db5e`.
2. **Squash and merge (PR #5):** Gộp toàn bộ các commit trên nhánh tính năng thành 1 commit duy nhất `a11fdc0: feat: add search_by_title function (#5)`.
3. **Rebase and merge (PR #6):** Tạo lịch sử tuyến tính trực tiếp trên `master` với SHA commit mới `32f017b: docs: add use case diagram`.

---

## 4. Issue (Truy vết Issue ⇄ Nhánh ⇄ Commit ⇄ PR)

| Issue | Tiêu đề Issue | Nhãn | Trạng thái | Đóng bởi Commit / PR |
|:---:|:---|:---:|:---:|:---|
| **#8** | Cart accepts the 21st DVD although the limit is 20 | `bug` | CLOSED | Commit `4c52f47` (`Fixes #8`) trong PR #9 |
| **#20** | search_by_title is case-sensitive (affects v1.0.0) | `bug` | CLOSED | Commit `a6008eb` / PR #22 (`Fixes #20`) |

### Vòng đời quản lý thay đổi (Change Control Lifecycle):
1. **Tiếp nhận & Ghi nhận:** Tạo Issue mô tả lỗi và điều kiện tái hiện.
2. **Tái hiện qua Test (FAIL trước):** Tạo nhánh riêng `bugfix/*` (hoặc `hotfix/*`), viết unit test mô tả hành vi lỗi và chạy test xác nhận thất bại.
3. **Khắc phục (PASS):** Sửa mã nguồn logic, chạy lại test xác nhận thành công.
4. **Liên kết truy vết:** Đưa từ khóa `Fixes #N` vào commit message và mô tả Pull Request.
5. **Duyệt & Tích hợp:** PR được review, merge vào nhánh đích và Issue tự động chuyển sang `CLOSED`.

---

## 5. GitHub Actions (CI)

Workflow CI (`.github/workflows/ci.yml`) tự động kích hoạt khi có Pull Request nhắm tới `master`, `release/**` hoặc push trực tiếp lên `master`:

| Thời điểm (UTC) | Sự kiện | Nhánh / PR | Tiêu đề Workflow Run | Kết quả |
|:---:|:---:|:---:|:---|:---:|
| 2026-11-07 12:20:06 | `push` | `master` | `Merge pull request #26 from NguyenThinh06/topic/ci-unit-tests` | **success** |
| 2026-11-07 12:19:43 | `pull_request` | `topic/ci-unit-tests` | `ci: add GitHub Actions workflow and lab 05 answers` | **success** |

Job `test` thực thi trên môi trường máy ảo Ubuntu với Python 3.12, chạy lệnh `python -m unittest discover -s tests -v`. Branch protection trên GitHub cấu hình bắt buộc check `test` phải pass mới cho phép hợp nhất PR vào `master`.

---

## 6. Status Accounting & Kiểm toán cấu hình (Lab 04–05)

### Ghi nhận trạng thái (Status Accounting):

```bash
# 1. Các commit chuẩn bị phát hành giữa v0.3.0 và v1.0.0
$ git log --oneline --no-merges v0.3.0..v1.0.0
2706d37 chore: prepare release 1.0.0

# 2. Các thay đổi trên master đi trước baseline release/lab04
$ git log --oneline release/lab04..master
b8e7bbb Merge pull request #26 from NguyenThinh06/topic/ci-unit-tests
d01e147 ci: add GitHub Actions workflow and lab 05 answers
f91fa81 Merge pull request #24 from NguyenThinh06/fix/update-search-functions
264ebc4 fix: ensure both search functions exist in aims/search.py
db53b6e fix: include search_by_title in aims/search.py
5b9551c Merge pull request #22 from NguyenThinh06/hotfix/search-case-insensitive-master
4deae9b docs: add 1.0.1 to changelog
a6008eb fix: make search_by_title case-insensitive
fffc964 Merge pull request #19 from NguyenThinh06/topic/prepare-release-1.1.0
170f5c7 chore: prepare release 1.1.0
7126cb3 Merge pull request #18 from NguyenThinh06/feature/search-by-category
73a51d9 feat: add search_by_category function
efa17e0 Merge pull request #17 from NguyenThinh06/topic/answers-lab04
cd2938c docs: add discussion answers for lab 03 and lab 04
652c2f1 Merge pull request #16 from NguyenThinh06/feature/sort-cart
9dcc7f1 feat: add sort_by_title and sort_by_cost to Cart

# 3. Thống kê tệp thay đổi giữa baseline v0.3.0 và v1.0.0
$ git diff --stat v0.3.0 v1.0.0
 CHANGELOG.md     | 19 +++++++++++++++++++
 aims/__init__.py |  1 +
 main.py          |  2 ++
 3 files changed, 22 insertions(+)

# 4. Thống kê tệp thay đổi giữa v1.0.0 và bản vá PATCH v1.0.1 (chỉ 4 tệp)
$ git diff --stat v1.0.0 v1.0.1
 CHANGELOG.md         |  4 +++-
 aims/__init__.py     |  2 +-
 aims/search.py       |  4 ++--
 tests/test_search.py | 15 +++++++++++++++
 4 files changed, 21 insertions(+), 4 deletions(-)

# 5. Định danh phiên bản hiện tại so với tag gần nhất
$ git describe --tags
v1.0.0-16-gb8e7bbb

# 6. Kiểm tra tệp rác trong baseline v1.0.0
$ git ls-tree -r --name-only v1.0.0
.gitattributes
.github/pull_request_template.md
.gitignore
CHANGELOG.md
README.md
aims/__init__.py
aims/cart.py
aims/dvd.py
aims/search.py
docs/answer-lab02.md
docs/answers-lab01.md
docs/use-case.md
main.py
tests/__init__.py
tests/test_cart.py
# (Không có bất kỳ tệp rác __pycache__ hay .venv nào)
```

### Kiểm toán đa phiên bản của Hotfix (Lab 05, Phần F):

```bash
# 1. Truy vết 2 commit cherry-pick từ commit gốc 6915240
$ git log --all --oneline --grep "cherry picked from commit 6915240"
0019e0d fix: make search_by_title case-insensitive
a6008eb fix: make search_by_title case-insensitive
# (Bản 0019e0d trên release/lab05; bản a6008eb trên master)

# 2. Tag chứa commit sửa lỗi gốc
$ git tag --contains 6915240
v1.0.1
```

### Kiểm tra hành vi đồng nhất trên cả 3 dòng phiên bản:
Thực hiện chạy kiểm thử tìm kiếm `"lion"` không phân biệt hoa thường trên cả ba dòng:
```bash
foreach ($ref in @("v1.0.1", "v1.1.0", "master")) {
    git switch --detach -q $ref
    $out = python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print(len(search_by_title([D('The Lion King')], 'lion')))"
    Write-Host "$ref : $out"
}
git switch -q master
```
**Kết quả kiểm toán:**
```text
v1.0.1 : 1
v1.1.0 : 1
master : 1
```

### Tái tạo phiên bản cũ (Configuration Audit):
1. **Kiểm tra phiên bản cũ với `detached HEAD`:**
   ```bash
   git switch --detach v0.2.0 && python main.py && git switch master
   ```
   Kết quả: `Total cost: 63.89 $` (đáp ứng đúng số kiểm tra chuẩn).
2. **Mở song song với `git worktree`:**
   ```bash
   git worktree add ../aims-v1.0.0 v1.0.0
   cd ../aims-v1.0.0 && python -m unittest discover -s tests -v
   cd ../aims && git worktree remove ../aims-v1.0.0
   ```
3. **Đóng gói phát hành với `git archive`:**
   ```bash
   git archive --format=zip --prefix=aims-1.0.0/ -o ../aims-1.0.0.zip v1.0.0
   ```
   Tệp lưu trữ `aims-1.0.0.zip` (9,186 bytes) được tạo độc lập, không chứa thư mục ẩn `.git`.

---

## 7. Việc đã làm & Bài học từ các sai sót thực tế

### Những việc đã hoàn thành:
- Thiết lập đầy đủ 5 nhánh `release/labXX` tương ứng với baseline nộp bài của từng bài Lab.
- Gắn đủ 6 annotated tag chuẩn ngữ nghĩa SemVer (`v0.1.0`, `v0.2.0`, `v0.3.0`, `v1.0.0`, `v1.0.1`, `v1.1.0`).
- Xuất bản 1 GitHub Release chính thức cho bản phát hành ổn định `v1.0.0`.
- Hoàn thành **24 Pull Request**, thực hành đủ 3 kiểu tích hợp (`Merge commit`, `Squash and merge`, `Rebase and merge`).
- Quản lý đóng 2 Issue lỗi tự động bằng từ khóa liên kết `Fixes #8` và `Fixes #20`.
- Tạo xung đột mã nguồn thật trong giỏ hàng (thông báo tiếng Việt vs tên đĩa) và giải quyết kết hợp cả hai ý đồ một cách hoàn hảo.
- Thực hành hoàn tác an toàn qua nhánh và PR bằng `git revert -m 1`.
- Lan truyền hotfix có chọn lọc bằng `git cherry-pick -x` trên 3 dòng mã song song (`release/lab04`, `master`, `release/lab05`).
- Thiết lập kiểm thử tích hợp liên tục CI tự động với GitHub Actions bảo vệ nhánh `master`.

### Bài học kinh nghiệm từ các tình huống thực tế:

1. **Sự cố lệch ngữ cảnh tệp khi cherry-pick hotfix trên nhánh đã phát triển tính năng mới:**
   - *Tình huống:* Trong Lab 05, bản sửa lỗi `search_by_title` được tách từ baseline `v1.0.0` (khi đó tệp `aims/search.py` chỉ có 1 hàm). Trong khi đó, nhánh `master` và `release/lab05` đã được bổ sung hàm `search_by_category` từ trước. Khi thực hiện cherry-pick và merge hotfix, do sai lệch về ngữ cảnh mã nguồn, tệp `aims/search.py` bị mất một trong hai hàm trên các nhánh đích.
   - *Cách xử lý chuẩn SCM:* Tuyệt đối không dùng `git push --force` để ghi đè lịch sử. Em đã mở thêm 2 PR sửa đổi bổ sung: PR #24 (`fix/update-search-functions`) vào `master` và PR #25 (`fix/search-release-lab05`) vào `release/lab05` để khôi phục đầy đủ cả hai hàm tìm kiếm và bổ sung unit test kiểm chứng.
   - *Bài học:* Khi chuẩn bị commit hotfix trên nhánh release cũ, chỉ nên tác động vào đúng các dòng cần sửa; và sau khi cherry-pick phải chạy toàn bộ bộ test tổng hợp (`unittest discover`) trước khi gửi PR tích hợp.

2. **Vấn đề bảng mã ký tự (Encoding) tiếng Việt giữa môi trường Windows và CI Linux:**
   - *Tình huống:* Khi bổ sung câu thông báo tiếng Việt `"Đã thêm đĩa vào giỏ hàng"`, lệnh `python -m unittest` trên Windows PowerShell mặc định (`cp1252`) báo lỗi `UnicodeEncodeError`, trong khi workflow GitHub Actions chạy trên Ubuntu UTF-8 lại pass 100%.
   - *Cách xử lý:* Nắm rõ cơ chế I/O encoding của Python và thiết lập cờ `python -X utf8` hoặc biến môi trường `PYTHONUTF8=1` khi làm việc trên terminal Windows.
   - *Bài học:* Cấu hình tệp `.gitattributes` rõ ràng và luôn chủ động kiểm soát bảng mã của các chuỗi text đa ngôn ngữ khi phát triển ứng dụng đa nền tảng.

3. **Chính sách Branch Protection khi thực hành cá nhân:**
   - *Đặc điểm:* GitHub mặc định ngăn chặn tác giả tự approve Pull Request của chính mình (`"Can not approve your own pull request"`).
   - *Giải pháp:* Theo đúng chỉ dẫn thực hành cho sinh viên làm việc độc lập, đặt `Require approvals = 0` nhưng **vẫn giữ bắt buộc đi qua Pull Request** (`Require a pull request before merging`) và bắt buộc **CI status checks pass**. Nhờ đó, luồng làm việc vẫn đảm bảo 100% kỷ luật SCM: không commit thẳng lên master/release, mọi thay đổi đều được ghi vết, review Files changed và kiểm tra tự động trước khi tích hợp.
