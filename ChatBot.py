
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
import os

#load in variabels env
load_dotenv()

#streamlit page stup
st.set_page_config(
    page_title= "دستیار پیوند مهر",
    page_icon= "🤖",
    layout= "centered"
)

st.title("دستیار پشتیبانی پیوند مهرخوبان 💬")

#chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show history chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#llm init
llm = ChatOpenAI(
    model = "gpt-6.1-terra",
    base_url="https://api.avalai.ir/v1",
    temperature=0,

)

#prompt Tamplates
prompt_template = ChatPromptTemplate.from_messages([   
("system" , """ 
شما یک دستیار مهربان و پراز شور وانگیزه از موسسه پیوند مهرخوبان  برای پاسخ داده هستی\n
تنها منابع تو برای پاسخ دادن  متن زیر است:\n
{context}
قوانین :\n
1. برای پاسخ دادن فقط از اطلاعات داخل {context}استفاده می کنید\n
2.اگر پاسخ در {context}صادقانه بگو اطلاعاتی در باره این موضوع در منبع من نیست\n
3. هرگز از دانش عمومی و حدس  و گمان خودت استفاده نکن\n
4. پاسخ ها را به زبان فارسی و روان ارائه بده\n
"""),
    MessagesPlaceholder(variable_name= 'chat_history'), 
    ("user", "{input}")
])   

#user
user_prompt =st.chat_input("Ask ChatBot...")

chain = prompt_template |llm

if user_prompt :
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})    
    context_text = ("""
کانون پیوند مهر خوبان
مرکز تخصصی ازدواج جوانان و خانواده؛ مجموعه‌ای از همسان‌گزینی، مشاوره، آموزش، پژوهش، تسهیلات ازدواج و خدمات فرهنگی.
ادرس :اصفهان، خیابان آیت‌الله کاشانی، جنب خیابان میرداماد

خدمات مجموعه :
همسان گزینی تخصصی:

فرایند همسان‌گزینی با تکمیل اطلاعات، ارزیابی و همراهی کارشناسان انجام می‌شود تا تصمیم‌گیری از یک مسیر روشن و مسئولانه عبور کند.
مراحل همسان گزینی عبارت است از :
۱
تشکیل پرونده
ثبت اطلاعات و تکمیل مرحله‌ای پروفایل
۲
شناخت و ارزیابی
پرسش‌نامه‌ها و بررسی تخصصی پرونده
۳
بررسی و معرفی
پیشنهاد متناسب و ادامه مسیر با نظارت کارشناس
اطلاعات پرونده در چارچوب فرایند تخصصی مجموعه بررسی می‌شود و دسترسی به آن محدود است.
تهسیلات ازدواج :
خدمات عقد و عروسی
دسترسی هماهنگ‌تر به خدمات مورد نیاز مراسم.
مشاوره تخصصی
مشاوره فردی، زوجی و خانواده و تربیت فرزند ا.
آموزش و کارگاه
یادگیری مهارت‌های انتخاب، ارتباط و زندگی مشترک.
محصولات فرهنگی
محتوای کاربردی حوزه ازدواج و خانواده.

راهنمای مسیر شروع :
مسیر شما در سامانه
ثبت نام امن :باشماره همراه خود یک حساب بسازید در سایت  و با ان وارد شوید 
2.تکمیل پروفایل: اطلاعات خود را مرحله به مرحله ثبت کنید
3.ارزیابی و مشاوره : ازمون ها و مراحل خود را انجام دهید
4.پیگیری نتیجه :وضعیت پرونده و معرفی ها و خدمات را  از پنل دنبال کنید

قابل اعتماد بودن سامانه 
اعتماد، قبل از هر انتخاب
اطلاعات شخصی شما یک مسئولیت است
شفافیت فرایند، دسترسی محدود به پرونده و همراهی تخصصی باید در تمام مسیر حفظ شود.

سوالات متداول که شاید کاربر بپرسد 
ثبت‌نام در سامانه چگونه انجام می‌شود؟ 
از طریق دکمه «شروع ثبت‌نام» حساب کاربری ایجاد می‌کنید؛ سپس مراحل تکمیل پرونده در پنل نمایش داده می‌شود.


آیا ثبت‌نام به معنی معرفی قطعی است؟
خیر. ثبت‌نام آغاز تشکیل پرونده است و ادامه مسیر به تکمیل اطلاعات، ارزیابی و بررسی تخصصی وابسته است.

اطلاعات پرونده چه کاربردی دارد؟
اطلاعات برای بررسی پرونده و ارائه خدمات مرتبط استفاده می‌شود و دسترسی به آن در چارچوب نقش‌های تعریف‌شده است.

اگر قبلاً ثبت‌نام کرده باشم چه کنم؟
از گزینه «ورود» یا «ورود با رمز یک‌بارمصرف» استفاده کنید و ادامه مراحل را در پنل ببینید.

آیا خدمات فقط شامل همسان‌گزینی است؟
خیر؛ مشاوره، آموزش، کافه ازدواج، اتاق عقد، خدمات مراسم، پژوهش و محصولات فرهنگی نیز ارائه می‌شوند.
""")


    reponse = chain.invoke({
        "context":context_text,
        "chat_history":st.session_state.chat_history[:-1], 
        "input":user_prompt,

    })

    assistant_response = reponse.content
    st.session_state.chat_history.append({"role":"assistant", "content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
