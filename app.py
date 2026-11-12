
 

  
   
import random
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components

# Cấu hình trang Web
st.set_page_config(
    page_title="SemiDesign AI - Thiết Kế Vi Mạch & STEM", layout="wide"
)

# Tiêu đề chính của dự án
st.title("🎛️ SemiDesign AI - Phần Mềm Thiết Kế Vi Mạch & Mô Phỏng STEM")
st.caption("Dự án tham gia Hội thi Học sinh phổ thông với ý tưởng khởi nghiệp")
st.divider()

# Chia giao diện chính thành 2 cột lớn
col_ai, col_lab = st.columns([1, 1.2], gap="large")

# =====================================================================
# CỘT 1: CÔNG NGHỆ CHUYÊN SÂU AI TỐI ƯU VI MẠCH (EDA)
# =====================================================================
with col_ai:
  st.header("🧠 1. Công nghệ Chuyên sâu AI Tối Ưu (EDA)")
  st.write(
      "Thuật toán AI tự động tìm vị trí đặt linh kiện giúp giảm thiểu tổng"
      " chiều dài dây dẫn trên bo mạch."
  )

  generations = st.slider(
      "Chọn số thế hệ AI học và thử nghiệm (Generations):",
      min_value=100,
      max_value=10000,
      value=2000,
      step=100,
  )

  components_list = [
      "Block_Power",
      "MCU_Core",
      "Gate_AND",
      "Gate_OR",
      "Output_LED",
  ]

  def tinh_chieu_dai_day(toa_do):
    tong_do_dai = 0
    for i in range(len(toa_do) - 1):
      # Lấy riêng tọa độ X [0] và tọa độ Y [1] để tính khoảng cách
      dx = abs(toa_do[i][0] - toa_do[i + 1][0])
      dy = abs(toa_do[i][1] - toa_do[i + 1][1])
      tong_do_dai += dx + dy
    return tong_do_dai

  if st.button("🚀 Chạy thuật toán AI tối ưu ngay", use_container_width=True):
    best_placement = None
    min_length = float("inf")

    for _ in range(generations):
      current_placement = [
          (random.randint(10, 90), random.randint(10, 90))
          for _ in components_list
      ]
      current_length = tinh_chieu_dai_day(current_placement)

      if current_length < min_length:
        min_length = current_length
        best_placement = current_placement

    st.success(
        "✅ Hoàn thành! Tổng chiều dài dây nối ngắn nhất tìm được:"
        f" **{min_length} mm**"
    )

    # Vẽ sơ đồ mặt bằng mạch điện tử (Lấy riêng X [0] và Y)
    fig, ax = plt.subplots(figsize=(5, 4.5))
    x_vals = [pos[0] for pos in best_placement]
    y_vals = [pos[1] for pos in best_placement]

    ax.plot(x_vals, y_vals, linestyle="--", color="#ff4b4b", linewidth=2)
    ax.scatter(x_vals, y_vals, color="#0068c9", s=180, zorder=5)

    for i, txt in enumerate(components_list):
      ax.annotate(
          f"{txt}\n({x_vals[i]}, {y_vals[i]})",
          (x_vals[i], y_vals[i]),
          textcoords="offset points",
          xytext=(0, 10),
          ha="center",
          fontsize=8,
          fontweight="bold",
      )

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("Sơ Đồ Bố Trí Mạch Tối Ưu Bởi AI", fontsize=11)
    ax.set_xlabel("Tọa độ trục X (mm)")
    ax.set_ylabel("Tọa độ trục Y (mm)")
    ax.grid(True, linestyle=":", alpha=0.6)

    st.pyplot(fig)

# =====================================================================
# CỘT 2: PHÒNG LAB ẢO MÔ PHỎNG STEM KIT (0 VNĐ)
# =====================================================================
with col_lab:
  st.header("🖥️ 2. Phòng Lab Mô Phỏng Trực Quan (0 VNĐ)")
  st.write(
      "Môi trường thực hành lắp ráp và kiểm thử mạch điện tử không cần mua phần"
      " cứng vật lý."
  )

  tab1, tab2 = st.tabs(
      ["🔌 Thực hành Cổng Logic Vi Mạch", "🤖 Mô phỏng Kit Arduino Thực Tế"]
  )

  # TAB 1: THÍ NGHIỆM CỔNG LOGIC SỐ
  with tab1:
    st.subheader("Bộ thí nghiệm Cổng Logic Bán Dẫn")
    c_in, c_gate, c_out = st.columns([1, 1.3, 1])

    with c_in:
      st.markdown("**1. Nguồn vào**")
      input_a = st.toggle("Nguồn A (Input A)", value=True)
      input_b = st.toggle("Nguồn B (Input B)", value=False)
      st.info(f"A = **{int(input_a)}** | B = **{int(input_b)}**")

    with c_gate:
      st.markdown("**2. Chọn Vi mạch**")
      gate_type = st.selectbox(
          "Loại cổng xử lý:",
          [
              "Cổng AND (Nhân logic)",
              "Cổng OR (Cộng logic)",
              "Cổng XOR (Loại trừ)",
              "Cổng NAND (Phủ định AND)",
          ],
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

  # TAB 2: NHÚNG KIT MÔ PHỎNG ARDUINO WOKWI
  with tab2:
    st.subheader("Thực hành lập trình & chạy thử mạch Vi điều khiển")
    kit_choice = st.radio(
        "Chọn bộ Kit thí nghiệm:",
        [
            "Kit 1: Trò chơi trí nhớ Simon Game (Arduino + LED 7 đoạn)",
            "Kit 2: Hệ thống điều khiển 32 Động cơ Servo (Arduino Mega)",
        ],
        horizontal=False,
    )

    if "Kit 1" in kit_choice:
      wokwi_url = "https://wokwi.com"
      st.caption(
          "👉 Nhấn nút Play màu xanh lá trên mạch để chơi thử và xem điểm số"
          " trên LED 7 đoạn."
      )
    else:
      wokwi_url = "https://wokwi.com"
      st.caption(
          "👉 Nhấn nút Play màu xanh lá để quan sát 32 động cơ Servo chạy hiệu"
          " ứng sóng và la bàn."
      )

    components.iframe(wokwi_url, height=500, scrolling=True)
