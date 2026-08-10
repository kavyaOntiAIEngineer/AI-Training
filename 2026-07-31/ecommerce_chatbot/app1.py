import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import time

# PAGE SETTINGS
st.set_page_config(
    page_title="ShopMate AI",
    page_icon="🛍️",
    layout="wide"
)

# SAMPLE DATA
data = pd.DataFrame({
    "Product": [
        "Wireless Headphones",
        "Smartphone",
        "Laptop",
        "Running Shoes",
        "Smart Watch",
        "Digital Camera",
        "Bluetooth Speaker",
        "Gaming Mouse"
    ],
    "Category": [
        "Electronics",
        "Electronics",
        "Electronics",
        "Fashion",
        "Electronics",
        "Electronics",
        "Electronics",
        "Electronics"
    ],
    "Price": [
        2999, 24999, 54999, 3999,
        5999, 45999, 3499, 1999
    ],
    "Rating": [
        4.5, 4.4, 4.7, 4.3,
        4.6, 4.8, 4.2, 4.4
    ]
})

# DARK THEME
st.markdown("""
<style>

.stApp {
    background-color: #070B14;
    color: #F8FAFC;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background-color: #0D1422;
}

[data-testid="stSidebar"] * {
    color: white;
}

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: #00E5FF;
    text-shadow: 0px 0px 18px rgba(0,229,255,0.5);
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #CBD5E1;
    margin-bottom: 25px;
}

.section-title {
    color: #00E5FF;
    font-size: 28px;
    font-weight: bold;
    margin-top: 15px;
}

.card {
    background-color: #111827;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #263449;
    margin-bottom: 15px;
}

.chat-box {
    background-color: #111827;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #00E5FF;
}

.stButton > button {
    width: 100%;
    background-color: #00C6FF;
    color: black;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px;
}

.stButton > button:hover {
    background-color: #008CBA;
    color: white;
}

[data-testid="stMetric"] {
    background-color: #111827;
    border: 1px solid #263449;
    padding: 15px;
    border-radius: 15px;
}

[data-testid="stExpander"] {
    background-color: #111827;
    border: 1px solid #263449;
    border-radius: 15px;
}

.footer {
    text-align: center;
    padding: 30px;
    color: #94A3B8;
}

.footer-title {
    color: #00E5FF;
    font-size: 25px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# SIDEBAR
st.sidebar.title("🛍️ ShopMate AI")
st.sidebar.write("Your Personal E-Commerce Assistant")
st.sidebar.divider()

page = st.sidebar.selectbox(
    "📌 Navigation",
    [
        "🏠 Home",
        "🛒 Products",
        "🤖 AI Chatbot",
        "📊 Analytics",
        "ℹ️ About"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("🔎 Shopping Filters")

category = st.sidebar.selectbox(
    "📦 Product Category",
    [
        "All",
        "Electronics",
        "Fashion",
        "Beauty",
        "Home & Kitchen"
    ]
)

max_price = st.sidebar.slider(
    "💰 Maximum Price",
    500,
    100000,
    50000,
    step=500
)

rating = st.sidebar.slider(
    "⭐ Minimum Rating",
    1.0,
    5.0,
    4.0,
    0.5
)

discount = st.sidebar.checkbox(
    "🏷️ Discounted Products"
)

st.sidebar.divider()
st.sidebar.success("🟢 ShopMate AI Online")


# HOME PAGE
if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🛍️ ShopMate AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        '✨ Discover • Compare • Shop Smarter'
        '</div>',
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d",
        use_container_width=True
    )

    st.success(
        "👋 Welcome to ShopMate AI! "
        "Your personal e-commerce shopping assistant."
    )

    st.divider()

    # CATEGORY SECTION
    st.markdown(
        '<div class="section-title">🛍️ Shop by Category</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1498049794561-7780e7231661",
            use_container_width=True
        )
        st.subheader("📱 Electronics")
        st.caption("Phones • Laptops • Gadgets")

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1445205170230-053b83016050",
            use_container_width=True
        )
        st.subheader("👕 Fashion")
        st.caption("Clothes • Shoes • Accessories")

    with col3:
        st.image(
            "https://images.unsplash.com/photo-1596462502278-27bfdc403348",
            use_container_width=True
        )
        st.subheader("💄 Beauty")
        st.caption("Makeup • Skincare • Care")

    with col4:
        st.image(
            "https://images.unsplash.com/photo-1556911220-bff31c812dba",
            use_container_width=True
        )
        st.subheader("🏠 Home")
        st.caption("Kitchen • Furniture • Decor")

    st.divider()

    # METRICS
    st.markdown(
        '<div class="section-title">📊 ShopMate Overview</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📦 Products", "120+", "+12")

    with c2:
        st.metric("🛒 Orders", "850", "+18%")

    with c3:
        st.metric("⭐ Average Rating", "4.5", "+0.2")

    with c4:
        st.metric("💰 Revenue", "₹10 Lakhs", "+20%")

    st.divider()

    # MEDIA
    st.markdown(
        '<div class="section-title">🎬 Shopping Experience</div>',
        unsafe_allow_html=True
    )

    media1, media2 = st.columns(2)

    with media1:
        st.image(
            "https://images.unsplash.com/photo-1556740749-887f6717d7e4",
            use_container_width=True
        )

    with media2:
        st.subheader("✨ Shop Smarter")
        st.write(
            "ShopMate AI helps users discover products, "
            "compare prices and make better shopping decisions."
        )
        st.info("🛍️ Search • Compare • Filter • Shop")

    st.divider()

    # STATUS FEATURES
    st.markdown(
        '<div class="section-title">⚡ Product Search Demo</div>',
        unsafe_allow_html=True
    )

    if st.button("🔎 Search Products"):

        with st.spinner("Searching products..."):

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

        st.success("✅ Search completed successfully!")

    placeholder = st.empty()

    if st.button("📡 Check ShopMate Status"):

        placeholder.info("Checking system status...")

        time.sleep(1)

        placeholder.success(
            "🟢 ShopMate AI is online and ready!"
        )

    st.divider()

    # CHATBOT QUICK SEARCH
    st.markdown(
        '<div class="section-title">🤖 Ask ShopMate AI</div>',
        unsafe_allow_html=True
    )

    question = st.text_input(
        "💬 What are you looking for?",
        placeholder="Example: Suggest a laptop under ₹50,000"
    )

    if st.button("🚀 Find Products"):

        if question:

            with st.spinner("🤖 ShopMate AI is thinking..."):
                time.sleep(2)

            st.success("Products found!")

            st.write(
                f"🔎 You searched for: **{question}**"
            )

            st.info(
                "💡 Compare price, rating, reviews and features "
                "before purchasing."
            )

        else:
            st.warning(
                "Please enter your shopping requirement."
            )

    with st.expander("💡 How does ShopMate AI work?"):

        st.write("1️⃣ Enter your product requirement.")
        st.write("2️⃣ Select your budget and category.")
        st.write("3️⃣ ShopMate analyzes your request.")
        st.write("4️⃣ Products are recommended.")
        st.write("5️⃣ Compare products before purchasing.")


# PRODUCTS PAGE
elif page == "🛒 Products":

    st.markdown(
        '<div class="main-title">🛒 Products</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Find products that match your needs'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    filtered_data = data[
        (data["Price"] <= max_price) &
        (data["Rating"] >= rating)
    ]

    if category != "All":

        filtered_data = filtered_data[
            filtered_data["Category"] == category
        ]

    search = st.text_input(
        "🔎 Search Product",
        placeholder="Example: Laptop"
    )

    if search:

        filtered_data = filtered_data[
            filtered_data["Product"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.write(
        f"🛍️ **{len(filtered_data)} products found**"
    )

    st.divider()

    # PRODUCT CARDS
    st.markdown(
        '<div class="section-title">⭐ Popular Products</div>',
        unsafe_allow_html=True
    )

    products = [
        (
            "Wireless Headphones",
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e",
            "₹2,999",
            "⭐ 4.5"
        ),
        (
            "Smartphone",
            "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9",
            "₹24,999",
            "⭐ 4.4"
        ),
        (
            "Laptop",
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853",
            "₹54,999",
            "⭐ 4.7"
        )
    ]

    col1, col2, col3 = st.columns(3)

    for col, product in zip(
        [col1, col2, col3],
        products
    ):

        with col:

            st.image(
                product[1],
                use_container_width=True
            )

            st.subheader(product[0])

            st.write(
                f"💰 **{product[2]}**"
            )

            st.write(product[3])

            if st.button(
                "🛒 Add to Cart",
                key="cart_" + product[0]
            ):
                st.success("Added to cart!")

    st.divider()

    # DATASET
    st.markdown(
        '<div class="section-title">📋 Product Dataset</div>',
        unsafe_allow_html=True
    )

    st.dataframe(
        filtered_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # VISUALIZATION
    st.markdown(
        '<div class="section-title">📈 Product Visualizations</div>',
        unsafe_allow_html=True
    )

    if len(filtered_data) > 0:

        chart_data = filtered_data.set_index("Product")

        st.subheader("📈 Native Line Chart")

        st.line_chart(
            chart_data["Price"]
        )

        st.subheader("📊 Native Bar Chart")

        st.bar_chart(
            chart_data["Price"]
        )

        st.subheader("📉 Native Area Chart")

        st.area_chart(
            chart_data["Rating"]
        )

        # MATPLOTLIB
        st.subheader("📐 Matplotlib Chart")

        fig, ax = plt.subplots()

        ax.plot(
            filtered_data["Product"],
            filtered_data["Price"],
            marker="o"
        )

        ax.set_title("Product Price Comparison")
        ax.set_xlabel("Product")
        ax.set_ylabel("Price")

        plt.xticks(
            rotation=30,
            ha="right"
        )

        plt.tight_layout()

        st.pyplot(fig)

        # PLOTLY
        st.subheader("✨ Interactive Plotly Chart")

        fig = px.bar(
            filtered_data,
            x="Product",
            y="Price",
            color="Category",
            hover_data=["Rating"],
            title="Interactive Product Price Comparison"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.warning(
            "No products match the selected filters."
        )

    st.divider()

    # UPLOAD DATASET
    st.markdown(
        '<div class="section-title">📂 Upload Product Dataset</div>',
        unsafe_allow_html=True
    )

    uploaded = st.file_uploader(
        "Upload Product CSV",
        type=["csv"]
    )

    if uploaded:

        df = pd.read_csv(uploaded)

        st.success(
            "✅ Product dataset uploaded successfully!"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    # DOWNLOAD DATASET
    st.subheader("📥 Download Product Data")

    csv = data.to_csv(
        index=False
    )

    st.download_button(
        label="⬇️ Download Product CSV",
        data=csv,
        file_name="shopmate_products.csv",
        mime="text/csv"
    )


# AI CHATBOT PAGE
elif page == "🤖 AI Chatbot":

    st.markdown(
        '<div class="main-title">🤖 ShopMate AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Your Personal Shopping Assistant'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    with st.container():

        st.markdown(
            '<div class="chat-box">',
            unsafe_allow_html=True
        )

        st.subheader("🤖 ShopMate AI")

        st.write(
            "Hi! 👋 What can I help you find today?"
        )

        st.write("💡 Try asking:")

        st.write("🔹 Suggest a laptop under ₹50,000")
        st.write("🔹 Recommend good headphones")
        st.write("🔹 Find a smartphone")

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    st.write("")

    question = st.text_input(
        "💬 Type your question",
        placeholder="Ask ShopMate something..."
    )

    if st.button("🚀 Ask ShopMate AI"):

        if question:

            with st.spinner(
                "🤖 ShopMate AI is thinking..."
            ):

                time.sleep(2)

            st.success(
                "ShopMate AI Response"
            )

            st.write(
                f"🧑 **You:** {question}"
            )

            st.write(
                "🤖 **ShopMate AI:** "
                "Based on your requirement, I recommend "
                "checking products with good ratings, "
                "reasonable prices and positive reviews."
            )

        else:

            st.warning(
                "Please type your question first."
            )

    with st.expander(
        "🧠 What can I ask ShopMate AI?"
    ):

        st.write("🔎 Product recommendations")
        st.write("💰 Budget-based suggestions")
        st.write("⭐ Rating comparisons")
        st.write("🏷️ Discount information")
        st.write("📦 Product categories")


# ANALYTICS PAGE
elif page == "📊 Analytics":

    st.markdown(
        '<div class="main-title">📊 Shop Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Product and shopping insights'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📦 Products", "120+", "+12")

    with c2:
        st.metric("⭐ Average Rating", "4.5", "+0.2")

    with c3:
        st.metric("🛒 Orders", "850", "+18%")

    with c4:
        st.metric("💰 Revenue", "₹10 Lakhs", "+20%")

    st.divider()

    st.subheader("📊 Product Prices")

    st.bar_chart(
        data.set_index("Product")["Price"]
    )

    st.subheader("📈 Product Ratings")

    st.line_chart(
        data.set_index("Product")["Rating"]
    )

    st.subheader("✨ Price vs Rating")

    fig = px.scatter(
        data,
        x="Price",
        y="Rating",
        size="Price",
        color="Category",
        hover_name="Product",
        title="Product Price vs Rating"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("⚡ Application Status")

    status = st.empty()

    if st.button("🔄 Check Application Status"):

        with st.spinner(
            "Checking application..."
        ):

            time.sleep(2)

        status.success(
            "🟢 ShopMate AI is running normally!"
        )


# ABOUT PAGE
elif page == "ℹ️ About":

    st.markdown(
        '<div class="main-title">ℹ️ About ShopMate AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'A smart e-commerce shopping experience'
        '</div>',
        unsafe_allow_html=True
    )

    st.image(
        "https://images.unsplash.com/photo-1556740749-887f6717d7e4",
        use_container_width=True
    )

    st.write(
        "ShopMate AI is an E-Commerce Shopping Assistant "
        "built using Python and Streamlit."
    )

    st.write(
        "The application helps users explore products, "
        "filter products, compare prices, visualize data "
        "and interact with a shopping assistant."
    )

    st.divider()

    st.markdown(
        '<div class="section-title">✨ Application Features</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("✅ Product Search")
        st.write("✅ Category Filtering")
        st.write("✅ Price Filtering")
        st.write("✅ Rating Filtering")
        st.write("✅ Product Comparison")
        st.write("✅ Data Visualization")

    with col2:
        st.write("✅ AI Shopping Assistant")
        st.write("✅ Product Images")
        st.write("✅ Metrics")
        st.write("✅ Progress Bar")
        st.write("✅ CSV Upload")
        st.write("✅ CSV Download")

    with st.expander("🛠️ Technologies Used"):

        st.write("🐍 Python")
        st.write("🎈 Streamlit")
        st.write("🐼 Pandas")
        st.write("📊 Matplotlib")
        st.write("✨ Plotly")


# FOOTER
st.divider()

st.markdown(
    """
    <div class="footer">

        <div class="footer-title">
            🛍️ ShopMate AI
        </div>

        <p>
            ✨ Discover • Compare • Shop Smarter
        </p>

        <p>
            🚀 Built using Python & Streamlit
        </p>

        <p>
            © 2026 ShopMate AI
        </p>

    </div>
    """,
    unsafe_allow_html=True
)