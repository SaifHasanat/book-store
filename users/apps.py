from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
# هذا السطر يخبر Django أنه عند إنشاء نماذج جديدة في تطبيقك، يجب استخدام نوع الحقل BigAutoField كمفتاح أساسي افتراضي.
# هذا يعني أنه عند إنشاء نموذج جديد، إذا لم تقم بتحديد نوع الحقل للمفتاح الأساسي، فسيقوم Django تلقائيًا بإنشاء حقل BigAutoField له.
# يعد استخدام BigAutoField خيارًا جيدًا في معظم الحالات، خاصةً إذا كنت تتوقع أن يحتوي تطبيقك على قاعدة بيانات كبيرة وعدد كبير من السجلات.
#  BigAutoField يمكنه استيعاب عدد أكبر بكثير من السجلات مقارنةً بـ AutoField. هذا يعني أنه يمكنك إنشاء علاقات بين الجداول التي تحتوي على عدد كبير من السجلات.