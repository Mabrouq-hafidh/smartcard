from django.db import models


class Programme(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    programmes = models.ManyToManyField(
        Programme,
        related_name="courses"
    )

    def __str__(self):
        return f"{self.code} - {self.name}"

class Student(models.Model):
    student_id = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    programme = models.ForeignKey(
        Programme,
        on_delete=models.PROTECT,
        related_name="students"
    )

    year_of_study = models.PositiveIntegerField()

    date_of_birth = models.DateField(null=True, blank=True)

    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"


class SmartCard(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="smart_card"
    )

    card_uid = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)

    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_id} - {self.card_uid}"


class CourseRegistration(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="course_registrations"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    academic_year = models.CharField(max_length=20)
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.student_id} - {self.course.code}"