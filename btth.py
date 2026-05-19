from datetime import datetime

try:
    name = input("Nhập tên bệnh nhân: ").strip()
    birth_year = int(input("Nhập năm sinh: ").strip())
    sick_days = int(input("Nhập số ngày bị bệnh: ").strip())
    temperature = float(input("Nhập nhiệt độ cơ thể (°C): ").strip())
    medical_fee = float(input("Nhập chi phí khám: ").strip())

    current_year = datetime.now().year

    if (
        name == "" or
        birth_year < 1900 or birth_year > current_year or
        sick_days < 0 or
        temperature < 30 or temperature > 45 or
        medical_fee <= 0
    ):
        print("LỖI: Dữ liệu nhập vào không hợp lệ!")
        exit()   
    age = current_year - birth_year
    surcharge = medical_fee * 0.10
    total_fee = medical_fee + surcharge

    if temperature > 38 and sick_days > 3:
        health_status = "Nguy hiểm"

    elif temperature > 38:
        health_status = "Sốt cao"

    elif temperature > 37.5:
        health_status = "Sốt nhẹ"

    else:
        health_status = "Bình thường"

    if health_status == "Nguy hiểm":

        if age > 60:
            priority = "Cấp cứu"
        else:
            priority = "Ưu tiên cao"

    else:
        priority = "Bình thường"
    
    fee_level = "Cao" if total_fee > 500000 else "Thấp"
  
    print("\n--- KẾT QUẢ ---")
    print("Tên:", name)
    print("Tuổi:", age)
    print("Nhiệt độ:", temperature, "°C")
    print("Số ngày bệnh:", sick_days)

    print("\nTình trạng:", health_status)
    print("Mức độ ưu tiên:", priority)

    print("\nTổng chi phí:", total_fee, "VND")
    print("Mức chi phí:", fee_level)

except ValueError:
    print("LỖI: Dữ liệu nhập vào không hợp lệ!")