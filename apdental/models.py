from django.db import models

class SogeView(models.Model):
    chart = models.CharField(db_column='Chart', max_length=13, primary_key=True)
    Name = models.CharField(db_column='Name', max_length=100)
    first_day = models.DateTimeField(db_column='first_day', )
    Last_Day = models.DateTimeField(db_column='Last_Day', )
    Office = models.CharField(db_column='Office', max_length=15, )
    referkind = models.CharField(db_column='referkind', max_length=1, )
    h_zip = models.CharField(db_column='h_zip', max_length=6, )
    h_juso2 = models.CharField(db_column='h_juso2', max_length=100, )
    c_phone = models.CharField(db_column='c_phone', max_length=15, )
    h_phone = models.CharField(db_column='h_phone', max_length=15, )
    o_Phone = models.CharField(db_column='o_Phone', max_length=15, )
    chamgo = models.CharField(db_column='chamgo', max_length=100, )
    refer = models.CharField(db_column='refer', max_length=11, )
    referchart = models.CharField(db_column='referchart', max_length=20, )
    piboname = models.CharField(db_column='piboname', max_length=16, )
    jumin = models.CharField(db_column='jumin', max_length=13, )
    jongbeul = models.CharField(db_column='jongbeul', max_length=1, )
    k_number = models.CharField(db_column='k_number', max_length=15, )
    Kiho = models.CharField(db_column='Kiho', max_length=10, )
    kwan = models.CharField(db_column='kwan', max_length=1, )
    team = models.CharField(db_column='team', max_length=2, )
    chart2 = models.CharField(db_column='chart2', max_length=13, )

    class Meta:
        managed = False
        db_table = 'SogeView'

    def __str__(self):
        return "제목 : " + self.a_title + ", 유형 : " + self.a_type

class ImgInfo(models.Model):
    seq = models.IntegerField(db_column='seq', )
    chart = models.CharField(db_column='chart', max_length=13, )
    C_Date = models.DateTimeField(db_column='C_Date', )
    C_Type = models.IntegerField(db_column='C_Type', )
    C_SubType = models.IntegerField(db_column='C_SubType', )
    F_Type = models.IntegerField(db_column='F_Type', )
    Image_Pos = models.IntegerField(db_column='Image_Pos', )
    Tooth_Pos = models.IntegerField(db_column='Tooth_Pos', )
    Pano_Modality = models.IntegerField(db_column='Pano_Modality', )
    Ceph_Modality = models.IntegerField(db_column='Ceph_Modality', )
    Standard_Modality = models.IntegerField(db_column='Standard_Modality', )
    Camera_Modality = models.IntegerField(db_column='Camera_Modality', )
    CT_Modality = models.IntegerField(db_column='CT_Modality', )
    Pacs_Modality = models.IntegerField(db_column='Pacs_Modality', )
    PacsSModality = models.CharField(db_column='Pacs_SModality', max_length=32, )
    Comment = models.CharField(db_column='Comment', max_length=256, )
    CIPName = models.CharField(db_column='C_IPName', max_length=15, )
    I_TreatCode = models.IntegerField(db_column='I_TreatCode', )
    ISubTreatCode = models.CharField(db_column='I_SubTreatCode', max_length=64, )
    #sogeview_id = models.CharField(db_column='sogeview_id', ) # 추가 되야 됨 Fk  join(select_related) 이 가능
    sogeview = models.ForeignKey(SogeView, on_delete = models.CASCADE) #Fk 현제 table에 대상 table명+"_id"가 꼭 있어야 join(select_related) 이 가능 예)imginfo.sogeview_id
    #sogeview = models.OneToOneField("SogeView", on_delete = models.CASCADE)  #Fk 현제 table에 대상 table명+"_id"가 꼭 있어야 join(select_related) 이 가능 예)imginfo.sogeview_id


    class Meta:
        managed = False
        db_table = 'imginfo'

    def __str__(self):
        return "제목 : " + self.a_title + ", 유형 : " + self.a_type

class TbPatientInfo(models.Model):
    pnt_id = models.CharField(primary_key=True, db_column='pnt_id', max_length=8)
    pnt_int = models.IntegerField(db_column='pnt_int', default=0)
    pnt_name = models.CharField(db_column='pnt_name', max_length=18)
    resi_no = models.CharField(db_column='resi_no', max_length=7)
    doct_id = models.CharField(db_column='doct_id', max_length=5)
    img_id = models.CharField(db_column='img_id', max_length=1)
    insur_div1 = models.CharField(db_column='insur_div1', max_length=1)
    guild_dat1 = models.CharField(db_column='guild_dat1', max_length=8)
    guild_cd1 = models.CharField(db_column='guild_cd1', max_length=11)
    insur_no1 = models.CharField(db_column='insur_no1', max_length=13)
    insur_name1 = models.CharField(db_column='insur_name1', max_length=12)
    insur_rel1 = models.IntegerField(db_column='insur_rel1', default=0)
    insur_div2 = models.CharField(db_column='insur_div2', max_length=1)
    guild_dat2 = models.CharField(db_column='guild_dat2', max_length=8)
    guild_cd2 = models.CharField(db_column='guild_cd2', max_length=11)
    insur_no2 = models.CharField(db_column='insur_no2', max_length=13)
    insur_name2 = models.CharField(db_column='insur_name2', max_length=4)
    insur_rel2 = models.IntegerField(db_column='insur_rel2', default=0)
    insur_div3 = models.CharField(db_column='insur_div3', max_length=1)
    guild_dat3 = models.CharField(db_column='guild_dat3', max_length=8)
    guild_cd3 = models.CharField(db_column='guild_cd3', max_length=13)
    insur_no3 = models.CharField(db_column='insur_no3', max_length=4)
    insur_name3 = models.CharField(db_column='insur_name3', max_length=2)
    insur_rel3 = models.IntegerField(db_column='insur_rel3', default=0)
    birth_div = models.CharField(db_column='birth_div', max_length=8)
    birth_dat = models.CharField(db_column='birth_dat', max_length=1)
    patient_division_uid = models.IntegerField(db_column='patient_division_uid', default=0)
    hp_no = models.CharField(db_column='hp_no', max_length=26)
    email = models.CharField(db_column='email', max_length=16)
    home_tel = models.CharField(db_column='home_tel', max_length=6)
    home_zipcd = models.CharField(db_column='home_zipcd', max_length=60)
    home_addr = models.CharField(db_column='home_addr', max_length=60)
    home_addr2 = models.CharField(db_column='home_addr2', max_length=53)
    barcode = models.CharField(db_column='barcode', max_length=13)
    registration_date = models.CharField(db_column='registration_date', max_length=8)
    sms_use = models.IntegerField(db_column='sms_use', default=0)
    family_id = models.CharField(db_column='family_id', max_length=32)
    lastvisit_date = models.CharField(db_column='lastvisit_date', max_length=8)
    vip_code = models.IntegerField(db_column='vip_code', default=0)
    remark = models.CharField(db_column='remark', max_length=123)
    visit_route = models.CharField(db_column='visit_route', max_length=18)
    etc = models.CharField(db_column='etc', max_length=54)
    hygienist = models.CharField(db_column='hygienist', max_length=10)
    protector_hp = models.CharField(db_column='protector_hp', max_length=13)
    assent = models.IntegerField(db_column='assent', default=0)

    class Meta:
        managed = False
        db_table = 'TB_PATIENT_INFO'

    def __str__(self):
        return "ID : " + self.id

class TbReservation(models.Model):
    btime = models.IntegerField(db_column='btime', default=0)
    etime = models.IntegerField(db_column='etime', default=0)
    pnt = models.ForeignKey(TbPatientInfo, db_column='pnt_id', on_delete=models.CASCADE)
    #pnt_id = models.ForeignKey(TbPatientInfo, on_delete=models.CASCADE)
    #pnt_id = models.CharField(db_column='pnt_id', max_length=8)
    doct_id = models.CharField(db_column='doct_id', max_length=5)
    nurse_id = models.CharField(db_column='nurse_id', max_length=10)
    chair_id = models.CharField(db_column='chair_id', max_length=1)
    content = models.CharField(db_column='content', max_length=66)
    rtype = models.IntegerField(db_column='rtype', default=0)
    rflag = models.IntegerField(db_column='rflag', default=0)
    sms_use = models.CharField(db_column='sms_use', max_length=1)
    modify_btime = models.IntegerField(db_column='modify_btime', default=0)
    modify_etime = models.IntegerField(db_column='modify_etime', default=0)
    input_datetime = models.CharField(db_column='input_datetime', max_length=14)
    begin_datetime = models.CharField(db_column='begin_datetime', max_length=14)
    tooth_number = models.IntegerField(db_column='tooth_number', default=0)
    font_color = models.IntegerField(db_column='font_color', default=0)
    back_color = models.IntegerField(db_column='back_color', default=0)
    rsv_etc = models.CharField(db_column='rsv_etc', max_length=120)

    class Meta:
        managed = False
        db_table = 'TB_RESERVATION'

    def __str__(self):
        return "ID : " + self.id

class TbResveInfo(models.Model):
    pnt_id = models.CharField(db_column='pnt_id', max_length=5)
    begin_datetime = models.DateTimeField(db_column='begin_datetime' )
    font_color = models.CharField(db_column='font_color', max_length=3)
    back_color = models.CharField(db_column='back_color', max_length=9)
    pnt_name = models.CharField(db_column='pnt_name', max_length=4)
    resi_no = models.CharField(db_column='resi_no', max_length=7)
    expc_tm = models.IntegerField(db_column='expc_tm')
    dlay_mi = models.IntegerField(db_column='dlay_mi')
    arvl_tm = models.DateTimeField(db_column='arvl_tm' )
    end_tm = models.DateTimeField(db_column='end_tm')

    class Meta:
        managed = False
        db_table = 'TB_RESVE_INFO'

    def __str__(self):
        return "ID : " + self.id