from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.conf import settings
from .core.BaseModel import BaseModel

class School(BaseModel):
    school_name = models.CharField(max_length=100, unique=True)
    logo = models.TextField(max_length=1200)
    location = models.TextField(max_length=1200)

    class Meta:
        db_table = "schools"

    def __str__(self):
        return self.school_name


class Institute(BaseModel):
    institute_name = models.CharField(max_length=255, unique=True)
    logo = models.TextField(max_length=1200)
    school = models.ForeignKey(  # ✅ replaced `school_id = CharField`
        "School", on_delete=models.CASCADE, related_name="institutes"
    )
    
    class Meta:
        db_table = "institutes"

    def __str__(self):
        return self.institute_name


class Program(BaseModel):
    class ProgramStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=ProgramStatus.choices, default=ProgramStatus.ACTIVE
    )
    institute = models.ForeignKey(  # ✅ proper FK
        "Institute", on_delete=models.CASCADE, related_name="programs"
    )
    
    class Meta:
        db_table = "programs"

    def __str__(self):
        return self.name


class User(AbstractUser, BaseModel):
    class UserStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        SUSPENDED = "suspended", "Suspended"

    status = models.CharField(
        max_length=20, choices=UserStatus.choices, default=UserStatus.ACTIVE
    )
    institute = models.ForeignKey(  # ✅ Proper FK instead of CharField
        "Institute",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    
    class Meta:
        db_table = "users"

    def __str__(self):
        return self.username


class System(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    
    class Meta:
        db_table = "systems"

    def __str__(self):
        return self.name

class UserSystems(BaseModel):  # ✅ typo fixed: "UserSytems" → "UserSystems"
    user = models.ForeignKey(  # ✅ dropped `_id` suffix
        "User", on_delete=models.CASCADE, related_name="user_systems"
    )
    system = models.ForeignKey(
        "System", on_delete=models.CASCADE, related_name="system_users"
    )
    
    class Meta:
        db_table = "user_systems"

    def __str__(self):
        return f"User: {self.user.username}, System: {self.system.name}"


class Student(BaseModel):
    class StudentStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        GRADUATED = "graduated", "Graduated"
        DROPPED = "dropped", "Dropped"

    s_studentID = models.CharField(max_length=50, unique=True)
    program = models.ForeignKey(
        "Program", on_delete=models.CASCADE, related_name="students"
    )
    s_rfid = models.CharField(max_length=100, unique=True, null=True, blank=True)
    s_fname = models.CharField(max_length=100)
    s_mname = models.CharField(max_length=100, null=True, blank=True)
    s_lname = models.CharField(max_length=100)
    s_suffix = models.CharField(max_length=20, null=True, blank=True)
    s_email = models.EmailField(unique=True)
    s_set = models.CharField(max_length=50, null=True, blank=True)
    s_lvl = models.PositiveIntegerField()
    s_status = models.CharField(
        max_length=20, choices=StudentStatus.choices, default=StudentStatus.ACTIVE
    )
    s_image = models.ImageField(upload_to="students/", null=True, blank=True)
    
    class Meta:
        db_table = "students"

    def __str__(self):
        return f"{self.s_lname}, {self.s_fname} ({self.s_studentID})"  # ✅ fixed field names


class CollectionCategory(BaseModel):
    category_name = models.CharField(max_length=150)
    collection_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    institute = models.ForeignKey(
        "Institute", on_delete=models.CASCADE, related_name="collection_categories"
    )

    class Meta:
        db_table = "collection_categories"
        # ordering = ["category_name"]
        # unique_together = ("category_name", "institute")
        pass
    
    def __str__(self):
        return f"{self.category_name} ({self.collection_fee})"


class Fee(BaseModel):
    class FeeStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        PARTIAL = "partial", "Partial"
        PAID = "paid", "Paid"
        WAIVED = "waived", "Waived"
        OVERDUE = "overdue", "Overdue"

    class Semester(models.TextChoices):
        FIRST = "1st", "First Semester"
        SECOND = "2nd", "Second Semester"

    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="fees"
    )
    category = models.ForeignKey(
        "CollectionCategory", on_delete=models.CASCADE, related_name="fees"
    )
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=FeeStatus.choices, default=FeeStatus.PENDING
    )
    due_date = models.DateTimeField()
    issued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="issued_fees",
    )
    remarks = models.TextField(null=True, blank=True)
    academic_year = models.PositiveIntegerField()
    semester = models.CharField(
        max_length=10, choices=Semester.choices, default=Semester.FIRST
    )

    class Meta:
        db_table = "fees"
        indexes = [
            models.Index(fields=["student", "academic_year", "semester"]),
        ]

    def __str__(self):
        return f"{self.student.s_studentID} - {self.category.category_name} ({self.status})"


class AttendanceEvent(BaseModel):
    class EventStatus(models.TextChoices):
        UPCOMING = "upcoming", "Upcoming"
        ONGOING = "ongoing", "Ongoing"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    event_name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_status = models.CharField(
        max_length=20, choices=EventStatus.choices, default=EventStatus.UPCOMING
    )
    
    class Meta:
        db_table = "attendance_events"

    def __str__(self):
        return f"{self.event_name} ({self.get_event_status_display()})"


class AttendanceRecord(BaseModel):
    student = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="attendance_records"
    )
    attendance_event = models.ForeignKey(
        "AttendanceEvent", on_delete=models.CASCADE, related_name="attendance_records"
    )
    morning_check_in = models.DateTimeField(null=True, blank=True)
    morning_check_out = models.DateTimeField(null=True, blank=True)
    afternoon_check_in = models.DateTimeField(null=True, blank=True)
    afternoon_check_out = models.DateTimeField(null=True, blank=True)
    total_fines = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fee = models.ForeignKey(
        "Fee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="attendance_records",
    )
    date = models.DateField()
    
    class Meta:
        db_table = "attendance_records"

    def __str__(self):
        return f"{self.student.s_studentID} - {self.date}"
    

class EventSetting(BaseModel):
    class EventStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        CLOSED = "closed", "Closed"

    attendance_event = models.ForeignKey(
        "AttendanceEvent",
        on_delete=models.CASCADE,
        related_name="settings"
    )
    date = models.DateField()

    # Morning session
    checkin_start = models.DateTimeField()
    checkin_end = models.DateTimeField()
    checkout_start = models.DateTimeField()
    checkout_end = models.DateTimeField()

    # Afternoon session
    afternoon_checkin_start = models.DateTimeField(null=True, blank=True)
    afternoon_checkin_end = models.DateTimeField(null=True, blank=True)
    afternoon_checkout_start = models.DateTimeField(null=True, blank=True)
    afternoon_checkout_end = models.DateTimeField(null=True, blank=True)

    event_status = models.CharField(
        max_length=20,
        choices=EventStatus.choices,
        default=EventStatus.ACTIVE
    )

    class Meta:
        db_table = "event_settings"
        # ordering = ["date"]
        # unique_together = ("attendance_event", "date")  # avoid duplicate settings for same event/date
        pass

    def __str__(self):
        return f"{self.attendance_event.event_name} - {self.date}"
    


class Payment(BaseModel):
    class PaymentMethod(models.TextChoices):
        CASH = "cash", "Cash"
        GCASH = "gcash", "GCash"
        BANK = "bank", "Bank Transfer"
        ONLINE = "online", "Online Payment"
        OTHER = "other", "Other"

    fee = models.ForeignKey(
        "Fee",
        on_delete=models.CASCADE,
        related_name="payments"
    )
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH
    )
    received_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="received_payments"
    )
    payment_submission = models.ForeignKey(
        "PaymentSubmission",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="payments"
    )

    class Meta:
        db_table = "payments"
        # ordering = ["-created_at"]
        pass

    def __str__(self):
        return f"Payment {self.id} - {self.amount_paid} ({self.payment_method})"



class PaymentSubmission(BaseModel):
    class SubmissionStatus(models.TextChoices):
        PENDING = "pending", "Pending Review"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    student = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="payment_submissions"
    )
    fee = models.ForeignKey(
        "Fee",
        on_delete=models.CASCADE,
        related_name="payment_submissions"
    )
    screenshot = models.ImageField(
        upload_to="payment_screenshots/",
        null=True,
        blank=True
    )  # screenshot_path
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2)
    reference_number = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=SubmissionStatus.choices,
        default=SubmissionStatus.PENDING
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_submissions"
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "payment_submissions"
        # ordering = ["-created_at"]
        pass
    
    def __str__(self):
        return f"Submission {self.id} - {self.student.student_id} ({self.status})"

