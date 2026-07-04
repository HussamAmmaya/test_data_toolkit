## الدوال (Functions)
- `read_test_data(path)` — تقرأ ملف (CSV) وترجّع قائمة قواميس (list of dicts).
- `get_value_by_key(records, key)` — تستخرج قيم حسب مفتاح (key).
- `send_result_to_file(results, path)` — تكتب النتائج لملف.

## التشغيل

```bash
python -m venv venv
venv\Scripts\activate      # على Windows
pip install -r requirements.txt
```

## تشغيل الاختبارات (Tests)

```bash
pytest
```

تشغيل بس الاختبارات السريعة (smoke tests):
```bash
pytest -m smoke
```

## المتطلبات (Requirements)
راجع `requirements.txt`.