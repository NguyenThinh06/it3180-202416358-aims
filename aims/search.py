def search_by_category(items, category):
    """Tìm các đĩa DVD theo thể loại (không phân biệt hoa thường)."""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]


def search_by_title(items, keyword):
    """Tìm các đĩa DVD có tiêu đề chứa keyword (không phân biệt hoa thường)."""
    return [dvd for dvd in items if keyword.lower() in dvd.title.lower()]
