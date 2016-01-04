# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AvailabilityStatus(models.Model):
    avl_status_id = models.AutoField(db_column='Avl_Status_Id', primary_key=True)  # Field name made lowercase.
    avl_status_name = models.CharField(db_column='Avl_Status_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    avl_status_remarks = models.CharField(db_column='Avl_Status_Remarks', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'availability_status'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MaterialClass(models.Model):
    material_class_id = models.IntegerField(db_column='Material_Class_ID', primary_key=True)
    # Field name made lowercase.
    material_class_manufacturer = models.CharField(db_column='Material_Class_Manufacturer', max_length=100, blank=True,
                                                   null=True)  # Field name made lowercase.
    material_class_manufac_part_no = models.CharField(db_column='Material_Class_Manufac_part_no', max_length=100,
                                                      blank=True, null=True)  # Field name made lowercase.
    material_class_handling = models.CharField(db_column='Material_Class_Handling', max_length=100, blank=True,
                                               null=True)  # Field name made lowercase.
    material_class_cleaning = models.CharField(db_column='Material_Class_Cleaning', max_length=100, blank=True,
                                               null=True)  # Field name made lowercase.
    material_class_disposition = models.CharField(db_column='Material_Class_Disposition', max_length=100, blank=True,
                                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'material_class'


class MovementFunction(models.Model):
    movement_function_id = models.FloatField(db_column='Movement_Function_ID', primary_key=True)
    # Field name made lowercase.
    movement_function_name = models.CharField(db_column='Movement_Function_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    movement_function_version = models.CharField(db_column='Movement_Function_Version', max_length=45, blank=True,
                                                 null=True)  # Field name made lowercase.
    movement_function_date = models.DateTimeField(db_column='Movement_Function_Date', blank=True, null=True)
    # Field name made lowercase.
    movement_function_status = models.ForeignKey(AvailabilityStatus, models.DO_NOTHING,
                                                 db_column='Movement_Function_Status', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movement_function'


class Movements(models.Model):
    movements_id = models.FloatField(db_column='Movements_ID', primary_key=True)  # Field name made lowercase.
    movements_function = models.ForeignKey(MovementFunction, models.DO_NOTHING, db_column='Movements_Function_ID',
                                           blank=True, null=True)  # Field name made lowercase.
    movements_params = models.CharField(db_column='Movements_Params', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    movements_short_name = models.CharField(db_column='Movements_Short_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    movements_long_name = models.CharField(db_column='Movements_Long_Name', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    movements_version = models.CharField(db_column='Movements_Version', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    movements_created_date = models.DateTimeField(db_column='Movements_Created_Date', blank=True, null=True)
    # Field name made lowercase.
    movements_status = models.ForeignKey('MvmtStatus', models.DO_NOTHING, db_column='Movements_Status', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movements'


class MvmtStatus(models.Model):
    mvmt_status_id = models.AutoField(db_column='MVMT_Status_Id', primary_key=True)  # Field name made lowercase.
    mvmt_status_name = models.CharField(db_column='MVMT_Status_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    mvmt_status_remarks = models.CharField(db_column='MVMT_Status_Remarks', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mvmt_status'


class Organization(models.Model):
    org_id = models.CharField(db_column='Org_ID', primary_key=True, max_length=100)  # Field name made lowercase.
    org_name = models.TextField(db_column='Org_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organization'


class PerceptValStatus(models.Model):
    pval_status_id = models.AutoField(db_column='PVal_Status_Id', primary_key=True)
    # Field name made lowercase.
    pval_status_name = models.CharField(db_column='PVal_Status_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    pval_status_remarks = models.CharField(db_column='Pval_Status_Remarks', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'percept_val_status'


class Percepts(models.Model):
    percepts_id = models.AutoField(db_column='Percepts_ID', primary_key=True)  # Field name made lowercase.
    percepts_movement = models.ForeignKey(Movements, models.DO_NOTHING, db_column='Percepts_Movement_ID', blank=True,
                                          null=True)  # Field name made lowercase.
    percepts_signal = models.ForeignKey('Signal', models.DO_NOTHING, db_column='Percepts_Signal_ID', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'percepts'


class PerceptsValue(models.Model):
    percepts_value_id = models.FloatField(db_column='Percepts_Value_ID', primary_key=True)  # Field name made lowercase.
    percepts_test_m_trials = models.ForeignKey('TestMTrials', models.DO_NOTHING, db_column='Percepts_Test_M_trials_ID',
                                               blank=True, null=True)  # Field name made lowercase.
    percepts_signal_id = models.FloatField(db_column='Percepts_Signal_ID', blank=True, null=True)
    # Field name made lowercase.
    percepts_value = models.CharField(db_column='Percepts_Value', max_length=512, blank=True, null=True)
    # Field name made lowercase.
    percepts_comments = models.CharField(db_column='Percepts_Comments', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    percepts_status = models.ForeignKey(PerceptValStatus, models.DO_NOTHING, db_column='Percepts_Status', blank=True,
                                        null=True)  # Field name made lowercase.
    percepts_value_percepts = models.ForeignKey(Percepts, models.DO_NOTHING, db_column='Percepts_Value_Percepts_ID',
                                                blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'percepts_value'


class ProcStep(models.Model):
    proc_step_id = models.IntegerField(db_column='Proc_Step_ID', primary_key=True)  # Field name made lowercase.
    proc_step_name = models.CharField(db_column='Proc_step_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proc_step'


class ProjStatusT(models.Model):
    proj_status_id = models.IntegerField(db_column='Proj_Status_ID', primary_key=True)  # Field name made lowercase.
    proj_status_name = models.CharField(db_column='Proj_Status_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    proj_status_remarks = models.CharField(db_column='Proj_Status_Remarks', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proj_status_t'


class Project(models.Model):
    project_id = models.FloatField(db_column='Project_ID', primary_key=True)  # Field name made lowercase.
    project_org = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Project_Org_ID')
    # Field name made lowercase.
    project_title = models.CharField(db_column='Project_Title', max_length=100)
    # Field name made lowercase.
    project_client_ref = models.CharField(db_column='Project_Client_Ref', max_length=100, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project'


class ProjectMember(models.Model):
    project_member_id = models.AutoField(db_column='Project_Member_ID', primary_key=True)  # Field name made lowercase.
    project_member_name = models.CharField(db_column='Project_Member_Name', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    project_member_email = models.CharField(db_column='Project_Member_Email', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    project_member_phone = models.CharField(db_column='Project_Member_Phone', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    project_member_address = models.CharField(db_column='Project_Member_Address', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    project_member_org = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Project_Member_Org_ID',
                                           blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_member'


class ProjectMemberRole(models.Model):
    project_id = models.ForeignKey(Project, models.DO_NOTHING,
                                                    db_column='Project_Member_Role_Project_ID')
    # Field name made lowercase.
    member_id = models.ForeignKey(ProjectMember, models.DO_NOTHING,
                                                   db_column='Project_Member_Role_Member_ID')
    # Field name made lowercase.
    roles = models.CharField(db_column='Project_Member_Role_Roles',
                                                 max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_member_role'
        unique_together = (('project_id', 'member_id'),)


class ProjectStatus(models.Model):
    project_status_project = models.OneToOneField(Project, models.DO_NOTHING, db_column='Project_Status_Project_ID',
                                                  primary_key=True)  # Field name made lowercase.
    project_status_proc = models.ForeignKey(ProcStep, models.DO_NOTHING, db_column='Project_Status_Proc_ID',
                                            blank=True, null=True)  # Field name made lowercase.
    project_status_status = models.ForeignKey(ProjStatusT, models.DO_NOTHING, db_column='Project_Status_Status',
                                              blank=True, null=True)  # Field name made lowercase.
    project_status_date = models.DateTimeField(db_column='Project_Status_Date', blank=True, null=True)
    # Field name made lowercase.
    project_status_comment = models.CharField(db_column='Project_Status_Comment', max_length=512, blank=True,
                                              null=True)  # Field name made lowercase.
    project_status_admin_id = models.IntegerField(db_column='Project_Status_Admin_ID', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_status'


class ProjectSupplement(models.Model):
    project_supplement_project = models.OneToOneField(Project, models.DO_NOTHING,
                                                      db_column='Project_Supplement_Project_ID', primary_key=True)
    # Field name made lowercase.
    project_supplement_rush = models.IntegerField(db_column='Project_Supplement_Rush', blank=True, null=True)
    # Field name made lowercase.
    project_supplement_material_info = models.CharField(db_column='Project_Supplement_Material_Info', max_length=512,
                                                        blank=True, null=True)  # Field name made lowercase.
    project_supplement_objectives = models.CharField(db_column='Project_Supplement_Objectives', max_length=512,
                                                     blank=True, null=True)  # Field name made lowercase.
    project_supplement_internal_notes = models.CharField(db_column='Project_Supplement_Internal_Notes', max_length=512,
                                                         blank=True, null=True)  # Field name made lowercase.
    project_supplement_other_notes = models.CharField(db_column='Project_Supplement_Other_Notes', max_length=512,
                                                      blank=True, null=True)  # Field name made lowercase.
    project_supplement_internal_poc = models.TextField(db_column='Project_Supplement_Internal_POC', blank=True,
                                                       null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_supplement'


class ProjectTests(models.Model):
    project_tests_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='Project_Tests_Project_ID')
    # Field name made lowercase.
    project_tests_test = models.ForeignKey('Test', models.DO_NOTHING, db_column='Project_Tests_Test_ID')
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'project_tests'
        unique_together = (('project_tests_project', 'project_tests_test'),)


class RawData(models.Model):
    raw_data = models.OneToOneField('TestMTrials', models.DO_NOTHING, db_column='Raw_Data_Id', primary_key=True)
    # Field name made lowercase.
    raw_data_data = models.TextField(db_column='Raw_Data_Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'raw_data'


class Report(models.Model):
    report_id = models.FloatField(db_column='Report_ID', primary_key=True)  # Field name made lowercase.
    report_project = models.ForeignKey(Project, models.DO_NOTHING, db_column='Report_Project_ID', blank=True, null=True)
    # Field name made lowercase.
    report_name = models.CharField(db_column='Report_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    report_date = models.DateTimeField(db_column='Report_Date', blank=True, null=True)  # Field name made lowercase.
    report_template = models.CharField(db_column='Report_Template', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    report_specimen = models.CharField(db_column='Report_Specimen', max_length=1024, blank=True, null=True)
    # Field name made lowercase.
    report_tests_m_trials = models.CharField(db_column='Report_Tests_M_Trials', max_length=1024, blank=True,
                                             null=True)  # Field name made lowercase.
    report_percepts = models.ForeignKey(PerceptsValue, models.DO_NOTHING, db_column='Report_Percepts', blank=True,
                                        null=True)  # Field name made lowercase.
    report_percepts_status = models.ForeignKey(PerceptValStatus, models.DO_NOTHING, db_column='Report_Percepts_Status',
                                               blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report'


class ReportFields(models.Model):
    report_fields_id = models.FloatField(db_column='Report_Fields_ID', primary_key=True)  # Field name made lowercase.
    report_fields_report = models.ForeignKey(Report, models.DO_NOTHING, db_column='Report_Fields_Report_ID',
                                             blank=True, null=True)  # Field name made lowercase.
    report_fields_content = models.CharField(db_column='Report_Fields_Content', max_length=45, blank=True,
                                             null=True)  # Field name made lowercase.
    report_fields_field_id = models.FloatField(db_column='Report_Fields_Field_ID', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report_fields'


class ReportFigure(models.Model):
    report_figure_id = models.FloatField(db_column='Report_Figure_ID', primary_key=True)  # Field name made lowercase.
    report_figure_report = models.ForeignKey(Report, models.DO_NOTHING, db_column='Report_Figure_Report_ID',
                                             blank=True, null=True)  # Field name made lowercase.
    report_figure_figure = models.TextField(db_column='Report_Figure_Figure', blank=True, null=True)
    # Field name made lowercase.
    report_figure_caption = models.CharField(db_column='Report_Figure_Caption', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    report_figure_type = models.CharField(db_column='Report_Figure_Type', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'report_figure'


class ServiceLog(models.Model):
    service_log_machine = models.OneToOneField('TestMachine', models.DO_NOTHING, db_column='Service_Log_Machine_ID',
                                               primary_key=True)  # Field name made lowercase.
    service_log_date = models.DateTimeField(db_column='Service_Log_Date', blank=True, null=True)
    # Field name made lowercase.
    service_log_admin = models.CharField(db_column='Service_Log_Admin', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    service_log_notes = models.CharField(db_column='Service_Log_Notes', max_length=512, blank=True, null=True)
    # Field name made lowercase.
    service_log_status = models.CharField(db_column='Service_Log_Status', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service_log'


class Signal(models.Model):
    signal_id = models.FloatField(db_column='Signal_ID', primary_key=True)  # Field name made lowercase.
    signal_movement_function = models.ForeignKey(MovementFunction, models.DO_NOTHING,
                                                 db_column='Signal_Movement_Function_ID', blank=True, null=True)
    # Field name made lowercase.
    signal_name = models.CharField(db_column='Signal_Name', unique=True, max_length=45, blank=True, null=True)
    # Field name made lowercase.
    signal_date = models.DateTimeField(db_column='Signal_Date', blank=True, null=True)  # Field name made lowercase.
    signal_version = models.CharField(db_column='Signal_Version', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    signal_status = models.ForeignKey(AvailabilityStatus, models.DO_NOTHING, db_column='Signal_Status',
                                      blank=True, null=True)  # Field name made lowercase.
    signal_param = models.CharField(db_column='Signal_Param', max_length=512, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'signal'


class Specimen(models.Model):
    specimen_id = models.FloatField(db_column='Specimen_ID', primary_key=True)  # Field name made lowercase.
    specimen_name = models.CharField(db_column='Specimen_Name', max_length=256, blank=True, null=True)
    # Field name made lowercase.
    specimen_date = models.DateTimeField(db_column='Specimen_Date', blank=True, null=True)  # Field name made lowercase.
    specimen_class = models.ForeignKey(MaterialClass, models.DO_NOTHING, db_column='Specimen_Class', blank=True,
                                       null=True)  # Field name made lowercase.
    specimen_prep_notes = models.CharField(db_column='Specimen_Prep_Notes', max_length=512, blank=True, null=True)
    # Field name made lowercase.
    specimen_comments = models.CharField(db_column='Specimen_Comments', max_length=512, blank=True, null=True)
    # Field name made lowercase.
    specimen_current_disposition = models.CharField(db_column='Specimen_Current_Disposition', max_length=100,
                                                    blank=True, null=True)  # Field name made lowercase.
    specimen_final_disposition = models.CharField(db_column='Specimen_Final_Disposition', max_length=100, blank=True,
                                                  null=True)  # Field name made lowercase.
    specimen_display_number = models.IntegerField(db_column='Specimen_Display_Number', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'specimen'


class Standards(models.Model):
    standards_id = models.FloatField(db_column='Standards_ID', primary_key=True)  # Field name made lowercase.
    standards_name = models.CharField(db_column='Standards_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    standards_version = models.CharField(db_column='Standards_Version', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    standards_date = models.DateTimeField(db_column='Standards_Date', blank=True, null=True)
    # Field name made lowercase.
    standards_comments = models.CharField(db_column='Standards_Comments', max_length=512, blank=True, null=True)
    # Field name made lowercase.
    standards_signal = models.ForeignKey(Signal, models.DO_NOTHING, db_column='Standards_Signal_ID', blank=True,
                                         null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'standards'


class Test(models.Model):
    test_test_id = models.FloatField(db_column='Test_Test_ID', primary_key=True)  # Field name made lowercase.
    test_surface = models.ForeignKey(Specimen, models.DO_NOTHING, db_column='Test_Surface_ID')
    # Field name made lowercase.
    test_desired_orient = models.IntegerField(db_column='Test_Desired_Orient', blank=True, null=True)
    # Field name made lowercase.
    test_actual_orient = models.IntegerField(db_column='Test_Actual_Orient', blank=True, null=True)
    # Field name made lowercase.
    test_sequence = models.ForeignKey('TestSequence', models.DO_NOTHING, db_column='Test_Sequence_ID', blank=True,
                                      null=True)  # Field name made lowercase.
    test_operator = models.CharField(db_column='Test_Operator', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    test_bt_serial = models.CharField(db_column='Test_BT_Serial', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    test_bt_firmware = models.CharField(db_column='TEST_BT_Firmware', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    test_software_ver = models.CharField(db_column='Test_Software_Ver', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    test_before_picture = models.TextField(db_column='Test_Before_Picture', blank=True, null=True)
    # Field name made lowercase.
    test_after_picture = models.TextField(db_column='Test_After_Picture', blank=True, null=True)
    # Field name made lowercase.
    test_machine = models.ForeignKey('TestMachine', models.DO_NOTHING, db_column='Test_Machine_ID', blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'


class TestMTrials(models.Model):
    test_m_trials_id = models.FloatField(db_column='Test_M_Trials_ID', primary_key=True)  # Field name made lowercase.
    test_m_trials_test = models.ForeignKey(Test, models.DO_NOTHING, db_column='Test_M_Trials_Test_ID', blank=True,
                                           null=True)  # Field name made lowercase.
    test_m_trials_movement = models.ForeignKey(Movements, models.DO_NOTHING, db_column='Test_M_Trials_Movement_ID',
                                               blank=True, null=True)  # Field name made lowercase.
    test_m_trials_start_location = models.CharField(db_column='Test_M_Trials_Start_Location', max_length=45, blank=True,
                                                    null=True)  # Field name made lowercase.
    test_m_trials_status = models.ForeignKey('TmtStatus', models.DO_NOTHING, db_column='Test_M_Trials_Status_ID',
                                             blank=True, null=True)  # Field name made lowercase.
    test_m_trials_date = models.DateTimeField(db_column='Test_M_Trials_Date', blank=True, null=True)
    # Field name made lowercase.
    test_m_trials_comments = models.CharField(db_column='Test_M_Trials_Comments', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_m_trials'


class TestMachine(models.Model):
    test_machine_serial = models.FloatField(db_column='Test_Machine_Serial', primary_key=True)
    # Field name made lowercase.
    test_machine_org = models.ForeignKey(Organization, models.DO_NOTHING, db_column='Test_Machine_Org_ID', blank=True,
                                         null=True)  # Field name made lowercase.
    test_machine_version = models.CharField(db_column='Test_Machine_Version', max_length=45, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_machine'


class TestSequence(models.Model):
    test_seq_id = models.IntegerField(db_column='Test_Seq_ID', primary_key=True)  # Field name made lowercase.
    test_seq_name = models.CharField(db_column='Test_Seq_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    test_seq_standard = models.IntegerField(db_column='Test_Seq_Standard', blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test_sequence'


class Testtable(models.Model):
    username = models.CharField(max_length=45, blank=True, null=True)
    image = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testtable'


class TmtStatus(models.Model):
    tmt_status_id = models.AutoField(db_column='TMT_Status_ID', primary_key=True)  # Field name made lowercase.
    tmt_status_name = models.CharField(db_column='TMT_Status_Name', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    tmt_status_remarks = models.CharField(db_column='TMT_Status_Remarks', max_length=128, blank=True, null=True)
    # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmt_status'