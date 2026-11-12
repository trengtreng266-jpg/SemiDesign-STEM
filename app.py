import random
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang Web
st.set_page_config(
    page_title="SemiDesign AI - Ninh Bình", page_icon="🎛️", layout="wide"
)

# Tiêu đề chính của dự án
st.title("🎛️ SemiDesign AI - Phần Mềm Thiết Kế Vi Mạch & Mô Phỏng STEM")
st.caption(
    "Dự án tham gia Hội thi Học sinh phổ thông với ý tưởng khởi nghiệp tỉnh"
    " Ninh Bình"
)
st.divider()

# Chia giao diện chính thành 2 cột lớn
col_ai, col_lab = st.columns((1, 1.2), gap="large")

# =====================================================================
# CỘT 1: CÔNG NGHỆ CHUYÊN SÂU AI TỐI ƯU VI MẠCH (EDA)
# =====================================================================
with col_ai:
  st.header("🧠 1. Công nghệ Chuyên sâu AI Tối Ưu (EDA)")
  st.write(
      "Thuật toán di chuyển cấu trúc tự động, tối ưu vị trí linh kiện để giảm"
      " chiều dài dây dẫn và suy hao tín hiệu."
  )

  du_an_mach = st.selectbox(
      "Chọn vi mạch hệ thống cần xử lý:",
      (
          (
              "Mạch IoT cảnh báo lũ lụt & sạt lở ngầm (Vùng núi Nho Quan - Gia"
              " Viễn)"
          ),
          "Mạch cảm biến tưới tiêu thông minh (Vùng đồi dứa Tam Điệp)",
          "Mạch điều khiển hệ thống chiếu sáng thông minh (Cố đô Hoa Lư)",
      ),
  )

  if "lũ lụt" in du_an_mach:
    components_list = (
        "Pin_NangLuong",
        "ESP32_Core",
        "CamBien_Mua",
        "CamBien_DoAmDat",
        "Loa_CanhBao",
    )
  elif "tưới tiêu" in du_an_mach:
    components_list = (
        "Nguon_12V",
        "MCU_DieuKhien",
        "CamBien_pH",
        "Relay_Bom",
        "Module_LoRa",
    )
  else:
    components_list = (
        "Nguon_AC_DC",
        "ViXuLy_TrungTam",
        "CamBien_AnhSang",
        "Mach_Dimmer",
        "Den_LED",
    )

  generations = st.slider(
      "Chọn số thế hệ AI học và thử nghiệm (Generations):",
      min_value=200,
      max_value=10000,
      value=2000,
      step=200,
  )

  def tinh_chieu_dai_day(toa_do):
    tong_do_dai = 0
    for i in range(len(toa_do) - 1):
      x1, y1 = toa_do[i]
      x2, y2 = toa_do[i + 1]
      tong_do_dai += abs(x1 - x2) + abs(y1 - y2)
    return tong_do_dai

  if st.button(
      "🔥 KÍCH HOẠT AI TỐI ƯU SƠ ĐỒ BO MẠCH", use_container_width=True
  ):
    best_placement = None
    min_length = float("inf")

    for _ in range(generations):
      current_placement = tuple(
          (random.randint(15, 85), random.randint(15, 85))
          for _ in components_list
      )
      current_length = tinh_chieu_dai_day(current_placement)

      khoang_cach_hop_le = True
      for i in range(len(current_placement)):
        x1, y1 = current_placement[i]
        for j in range(i + 1, len(current_placement)):
          x2, y2 = current_placement[j]
          if abs(x1 - x2) < 12 and abs(y1 - y2) < 12:
            khoang_cach_hop_le = False
            break

      if khoang_cach_hop_le and current_length < min_length:
        min_length = current_length
        best_placement = current_placement

    if best_placement is None:
      best_placement = tuple((20 + i * 14, 25 + (i % 2) * 30) for i in range(5))
      min_length = tinh_chieu_dai_day(best_placement)

    st.success(
        "✅ Hoàn thành! Tổng chiều dài dây nối ngắn nhất đạt:"
        f" **{min_length} mm**"
    )

    fig, ax = plt.subplots(figsize=(5.5, 4.5))
    x_vals = tuple(x for x, y in best_placement)
    y_vals = tuple(y for x, y in best_placement)

    ax.plot(
        x_vals,
        y_vals,
        linestyle="--",
        color="#ff4b4b",
        linewidth=2,
        label="Đường mạch dẫn tối ưu",
    )
    ax.scatter(x_vals, y_vals, color="#0068c9", s=200, zorder=5)

    for i, txt in enumerate(components_list):
      ax.annotate(
          f"{txt}\n({x_vals[i]}, {y_vals[i]})",
          (x_vals[i], y_vals[i]),
          textcoords="offset points",
          xytext=(0, 12),
          ha="center",
          fontsize=8,
          fontweight="bold",
          bbox=dict(
              boxstyle="round,pad=0.2", fc="white", ec="#cccccc", alpha=0.85
          ),
      )

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("Sơ Đồ Bố Trí Bo Mạch Tối Ưu Bởi AI", fontsize=11)
    ax.set_xlabel("Tọa độ trục X (mm)")
    ax.set_ylabel("Tọa độ trục Y (mm)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper right")

    st.pyplot(fig)

# =====================================================================
# CỘT 2: PHÒNG LAB MÔ PHỎNG TRỰC QUAN (0 VNĐ)
# =====================================================================
with col_lab:
  st.header("🖥️ 2. Phòng Lab Mô Phỏng Trực Quan (0 VNĐ)")
  st.write(
      "Bản sao số (Digital Twin) kiểm thử mạch điện tử thời gian thực không"
      " cần mua phần cứng vật lý."
  )

  tab1, tab2, tab3 = st.tabs((
      "🔌 Cổng Logic Vi Mạch",
      "🤖 Bản sao số Kit Arduino (Wokwi)",
      "📚 Chế độ Ngoại tuyến (Offline)",
  ))

  # TAB 1: BỘ THÍ NGHIỆM CỔNG LOGIC BÁN DẪN
  with tab1:
    st.subheader("Bộ thí nghiệm Cổng Logic Bán Dẫn")
    c_in, c_gate, c_out = st.columns((1, 1.3, 1))

    with c_in:
      st.markdown("**1. Nguồn vào**")
      input_a = st.toggle("Nguồn A (Input A)", value=True)
      input_b = st.toggle("Nguồn B (Input B)", value=False)
      st.info(f"A = **{int(input_a)}** | B = **{int(input_b)}**")

    with c_gate:
      st.markdown("**2. Chọn Vi mạch**")
      gate_type = st.selectbox(
          "Loại cổng xử lý:",
          (
              "Cổng AND (Nhân logic)",
              "Cổng OR (Cộng logic)",
              "Cổng XOR (Loại trừ)",
              "Cổng NAND (Phủ định AND)",
          ),
      )

      if "AND" in gate_type and "NAND" not in gate_type:
        output = input_a and input_b
        formula = "Y = A . B"
      elif "OR" in gate_type and "XOR" not in gate_type:
        output = input_a or input_b
        formula = "Y = A + B"
      elif "XOR" in gate_type:
        output = input_a != input_b
        formula = "Y = A ⊕ B"
      else:
        output = not (input_a and input_b)
        formula = "Y = ¬(A . B)"

      st.caption(f"Công thức Boole: `{formula}`")

    with c_out:
      st.markdown("**3. Đèn LED ra**")
      if output:
        st.success("💡 ĐÈN SÁNG (Mức 1)")
      else:
        st.error("⚫ ĐÈN TẮT (Mức 0)")

  # TAB 2: MÔ PHỎNG BẢN SAO SỐ KIT ARDUINO / ESP32
  with tab2:
    st.subheader("Mô phỏng mạch ứng dụng thực tế (0 VNĐ)")
    kit_choice = st.radio(
        "Chọn mô hình mạch thực hành:",
        (
            "Mô hình 1: Trạm cảnh báo tín hiệu & Điều khiển 32 Servo (Nho Quan"
            " - Gia Viễn)",
            "Mô hình 2: Bộ xử lý phản xạ & Kiểm thử vi điều khiển (Simon Game"
            " Kit)",
        ),
        horizontal=False,
    )

    if "Mô hình 1" in kit_choice:
      wokwi_url = "https://wokwi.com"
      st.caption(
          "👉 Nhấn nút Play màu xanh lá trên mạch để chạy mô phỏng hệ thống"
          " truyền động."
      )
    else:
      wokwi_url = "https://wokwi.com"
      st.caption(
          "👉 Nhấn nút Play màu xanh lá để kiểm thử tín hiệu nút nhấn và LED 7"
          " đoạn."
      )

    components.iframe(wokwi_url, height=480, scrolling=True)

  # TAB 3: CHẾ ĐỘ NGOẠI TUYẾN & TRA CỨU NHANH
  with tab3:
    st.subheader("Cẩm nang Thực hành STEM & Bảng Chân Trị Vi Mạch")
    st.write(
        "Tài liệu tích hợp sẵn giúp học sinh vùng cao tra cứu nguyên lý mạch"
        " điện tử ngay cả khi mạng yếu."
    )

    st.markdown("""

        | Đầu vào A | Đầu vào B | Cổng AND (A.B) | Cổng OR (A+B) | Cổng XOR (A⊕B) |
        | :---: | :---: | :---: | :---: | :---: |
        | 0 | 0 | 0 | 0 | 0 |
        | 0 | 1 | 0 | 1 | 1 |
        | 1 | 0 | 0 | 1 | 1 |
        | 1 | 1 | 1 | 1 | 0 |
        """)

    st.info(
        "💡 Mẹo thiết kế: Giảm tổng chiều dài dây dẫn trên bo mạch giúp giảm"
        " điện trở ký sinh, tiết kiệm pin cho các trạm quan trắc đặt tại vùng"
        " núi."
    )

