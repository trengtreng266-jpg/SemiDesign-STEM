import streamlit as st
import time
# Kết nối trực tiếp với file thuật toán lõi ai_core.py vừa lưu
from ai_core import chay_ai_toi_uu_mach

# Cấu hình trang web góc rộng chuyên nghiệp
st.set_page_config(
    page_title="SemiDesign AI - Ninh Bình",
    page_icon="🎛️",
    layout="wide"
)

st.title("🎛️ SemiDesign AI - Phần Mềm Thiết Kế Vi Mạch & Mô Phỏng STEM")
st.caption("Dự án tham gia Cuộc thi Học sinh phổ thông với ý tưởng khởi nghiệp tỉnh Ninh Bình")
st.markdown("---")

# Chia màn hình thành 2 cột
col1, col2 = st.columns(2)

# ==============================================================================
# CỘT 1: KẾT NỐI TRỰC TIẾP VỚI THUẬT TOÁN LÕI (ai_core.py)
# ==============================================================================
with col1:
    st.header("🧠 1. Công Nghệ Lõi AI Tối Ưu (EDA)")
    st.subheader("Thuật toán Di truyền tự động hóa cấu trúc vi mạch")
    
    de_tai = st.selectbox(
        "Chọn hệ thống vi mạch cần xử lý:",
        [
            "Mạch IoT cảnh báo lũ lụt & sạt lở ngầm (Vùng núi Nho Quan - Gia Viễn)",
            "Mạch chip tưới tiêu tự động dưới rễ cây (Đồng dứa Đồng Giao - Tam Điệp)",
            "Mạch STEM cảm biến dây chuyền đóng gói (Đặc sản Cơm cháy Ninh Bình)"
        ]
    )
    
    if st.button("🔥 KÍCH HOẠT AI TỐI ƯU SƠ ĐỒ BO MẠCH", use_container_width=True):
        with st.spinner("Đang gọi thuật toán từ ai_core.py để tính toán 500 thế hệ..."):
            time.sleep(0.5)
            # Gọi trực tiếp hàm tính toán từ file ai_core.py
            ket_qua = chay_ai_toi_uu_mach()
            
        st.success("✅ AI ĐÃ TỐI ƯU CẤU TRÚC VI MẠCH THÀNH CÔNG!")
        
        # Hiển thị các chỉ số thực nghiệm từ ai_core.py
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Dây nối ban đầu", value=f"{ket_qua['chieu_dai_ban_dau']} mm")
        m2.metric(label="Sau khi AI tối ưu", value=f"{ket_qua['chieu_dai_toi_uu']} mm", delta=f"-{ket_qua['ty_le_tiet_kiem']}%")
        m3.metric(label="Chi phí phần cứng", value="0 VNĐ")
        
        st.write("📍 **Bảng tọa độ đặt linh kiện do AI xuất ra (mm):**")
        for ten, (x, y) in zip(ket_qua["linh_kien"], ket_qua["toa_do_toi_uu"]):
            st.code(f"+ {ten:<22}: X = {x:02d} mm, Y = {y:02d} mm")

# ==============================================================================
# CỘT 2: PHÒNG LAB MÔ PHỎNG TRỰC QUAN 0 VNĐ
# ==============================================================================
with col2:
    st.header("🖥️ 2. Phòng Lab Mô Phỏng Trực Quan 0 VNĐ")
    st.subheader("Bản sao số (Digital Twin) kiểm thử mạch thời gian thực")
    
    tab1, tab2, tab3 = st.tabs([
        "🌧️ Mạch Lũ Lụt (Nho Quan)", 
        "🍍 Mạch Tưới Tiêu (Tam Điệp)", 
        "📡 Chế độ Dự phòng (Offline)"
    ])
    
    with tab1:
        wokwi_url_1 = "https://wokwi.com"
        st.components.v1.html(
            f'<iframe src="{wokwi_url_1}" width="100%" height="480px" style="border:1px solid #ccc; border-radius: 8px;"></iframe>', 
            height=500
        )
        
    with tab2:
        wokwi_url_2 = "https://wokwi.com"
        st.components.v1.html(
            f'<iframe src="{wokwi_url_2}" width="100%" height="480px" style="border:1px solid #ccc; border-radius: 8px;"></iframe>', 
            height=500
        )

    with tab3:
        st.warning("⚠️ **Chế độ trình diễn Offline (Dùng khi phòng thi mất mạng Internet):**")
        do_am_dat = st.slider("Kéo thanh trượt giả lập mực nước/độ ẩm ngầm (%):", 0, 100, 35)
        if do_am_dat > 75:
            st.error(f"🚨 CẢNH BÁO KHẨN CẤP ({do_am_dat}%): Nguy cơ sạt lở cao! Đã kích hoạt còi hú 85dB trên mặt đất!")
        elif do_am_dat < 30:
            st.info(f"💧 THÔNG BÁO NÔNG NGHIỆP ({do_am_dat}%): Đất khô! Vi mạch tự động bật máy bơm tưới rễ.")
        else:
            st.success(f"✅ TRẠNG THÁI AN TOÀN ({do_am_dat}%): Môi trường dưới lòng đất ổn định.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Dự án Khởi nghiệp Học sinh phổ thông tỉnh Ninh Bình - SemiDesign AI</p>", unsafe_allow_html=True)
