import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
#import google.generativeai as genai
import base64





def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# 이미지를 base64로 변환
img_base641 = get_image_base64("./01.png")
img_base642 = get_image_base64("./02.png")
img_base643 = get_image_base64("./03.png")

# 메인 제목 (Streamlit 기본 스타일링)
st.title('Investment Portfolio Dashboard')

# CSS 스타일 추가 (UI 요소 스타일링)
st.markdown("""
    <style>
    .section-title {
        font-size: 50px;
        font-weight: bold;
        color: #34495E;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .input-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .input-item {
        margin: 0 10px;
    }
    .dataframe-container {
        text-align: center;
    }
     .keyword-container {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        background-color: rgba(211, 211, 211, 0.2);
        border-radius: 15px; 
    }
    .keyword_container2 {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;   


    }        
    .keyword-box {
        display: inline-block;
        padding: 5px 10px;
        margin: 5px;
        border-radius: 25px;
        background-color: #ADD8E6;
        color: #333;
        font-size: 13px;
    }
    .font-style {
        font-size: 14px;
        font-weight: bold;
        color: #000080;
        font-family: 'Arial';
    }
    </style>
""", unsafe_allow_html=True)


#------------------------- 함수정의 ---------------------------------------------------
# def Recommend():
#     # 2.Idenrify Top Performing Sectors
#     df_stock_market['recdate'] = pd.to_datetime(df_stock_market['recdate'])
#     latest_date = df_stock_market['recdate'].max()
#     recent_stock_data = df_stock_market[df_stock_market['recdate'] == latest_date]

#     # Compute average closing price by sector and extract the top 3 sectors
#     top_sectors_df = recent_stock_data.groupby('sector_name')['close'].mean().nlargest(3)
#     top_sectors = top_sectors_df.index.tolist()
#     print("Top Sectors:", top_sectors)
#     #3. Filter Funds Based on Top Sectors
#     # Filter funds related to top sectors (with equity allocation over 50%)
#     funds_in_top_sectors = df_fund_allocation[df_fund_allocation['saham'] > 50]

#     #3. Select High-Return Funds in Top Sectors
#     # Filter high-return funds within top sectors based on the most recent returns
#     recent_fund_returns = df_fund_return[df_fund_return['date'] == df_fund_return['date'].max()]
#     funds_in_top_sectors = funds_in_top_sectors.merge(recent_fund_returns, on='isin_code')

#     # Add latest NAV values from NAV data
#     recent_nav = df_fund_nav[df_fund_nav['date'] == df_fund_nav['date'].max()][['isin_code', 'value']]
#     recent_nav.columns = ['isin_code', 'latest_nav']
#     funds_in_top_sectors = funds_in_top_sectors.merge(recent_nav, on='isin_code')

#     # Recommend top funds based on highest returns
#     recommended_funds = funds_in_top_sectors.sort_values(by='oneyear', ascending=False).head(5)
#     #st.write("Recommended Hot Theme Funds:")
#     recommended_funds = recommended_funds[['isin_code', 'saham', 'oneyear', 'latest_nav']].head(1)
#     return recommended_funds
#    # dataframe(recommended_funds[['isin_code', 'saham', 'oneyear', 'latest_nav']].head(1))

def plot_nav_for_recommended_funds(recommended_funds):
    fig = go.Figure()
    
    for isin_code in recommended_funds['isin_code'].unique():
        # Filter NAV data for the specific fund
        nav_data = df_fund_nav[df_fund_nav['isin_code'] == isin_code].sort_values(by='date')
        nav_data['date'] = pd.to_datetime(nav_data['date'])
        
        # Add NAV trend line for each fund
        fig.add_trace(go.Scatter(
            x=nav_data['date'],
            y=nav_data['value'],
            mode='lines',
            name=f'Fund {isin_code}'
        ))

    # Configure graph layout
    fig.update_layout(
        title='NAV Trend',
        xaxis_title='Date',
        yaxis_title='NAV',
        template='plotly_white',
        
    )

    st.plotly_chart(fig)

# def Jemini(value,recommended_funds):
#     GOOGLE_API_KEY = 
#     genai.configure(api_key=GOOGLE_API_KEY)
#     model = genai.GenerativeModel('gemini-pro')
    
#     # values를 딕셔너리로 받아서 그 값들을 활용
#     prompt = f"""
#     You are an expert investment advisor at a leading financial institution. Your role is to create personalized fund recommendations that explain why a specific fund matches an investor's profile and goals. Your explanations should be clear, thorough, and educational, helping investors fully understand the reasoning behind their personalized recommendations.
    

#     Using these values, create a personalized recommendation following this specific template structure:

#     "As a {value['age']} year-old {value['life']} investor with {value['Inv_goal']} objectives, your profile indicates a strong appetite for growth opportunities combined with a {value['Risk']} approach over a mid to long-term investment horizon. 

#     Our recommended fund {recommended_funds['isin_code'].values[0]} features a stock allocation of {str(int(recommended_funds['saham'].values[0]))}%, demonstrating its equity-focused strategy, with a one-year return of {round(recommended_funds['oneyear'].values[0]*100, 2)}%. 

#     This alignment between your {value['Risk']} profile and {value['Inv_goal']} objectives, combined with the fund's high equity exposure and demonstrated performance track record, makes it a suitable choice for your investment strategy, particularly considering your {value['life']} stage and long-term investment horizon."
#     """

    # 모델에서 텍스트 생성
    #response = model.generate_content(prompt)
    #return response.text 

#------------------------------------------------------------------------------------

# 입력 필터

col1, col2 = st.columns([1, 1])


# 데이터 로드---------------------------------------------------------





df = pd.read_csv('./df10.csv')
df.index= range(1,len(df)+1)

#df_fund_allocation=pd.read_csv('./df_fund_allocation.csv')
df_fund_nav=pd.read_csv('./chart_ver.csv', index_col=0)
recommend=pd.read_csv('./recomended.csv', index_col=0)
#df_fund_return=pd.read_csv('./df_fund_return.csv')
#df_stock_market=pd.read_csv('./df_stock_market.csv')
#-------------------------------------------------------------------------------------




with col1:
    ID_input = st.text_input('Enter portfolio ID', placeholder=f'Enter your ID (1~{len(df)})', key='id_input')

# 입력값이 있을 때만 실행
if ID_input.isdigit():


    ID = int(ID_input)
    if ID > 10:
        st.warning("Please enter a portfolio ID between 1 ~ 10.", icon="⚠️")
    else:
        filtered_df = df[df.index == ID]
    # filtered_df
        age= filtered_df['age'].values[0]
        gen= filtered_df['Generation'].values[0]
        life= filtered_df['Life Stage'].values[0]
        inv_horizon= filtered_df['Investment Horizon'].values[0]
        Risk= filtered_df['Risk Tolerance'].values[0]
        Inv_goal=filtered_df['Investment Goal'].values[0]
        value = {
        'age': filtered_df['age'].values[0],
        'gen': filtered_df['Generation'].values[0],
        'life': filtered_df['Life Stage'].values[0],
        'inv_horizon': filtered_df['Investment Horizon'].values[0],
        'Risk': filtered_df['Risk Tolerance'].values[0],
        'Inv_goal': filtered_df['Investment Goal'].values[0]
        }
    

        # Investment Goal 박스
        # Investment Goal 박스
        st.markdown(f"""
            <div style="background-color:rgb(247, 251, 253); padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid gray; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <img src= "data:image/png;base64,{img_base641}" alt="image" style="width:20px; height:20px; vertical-align: middle; margin-right: 10px;">
                <span style='color: gray; font-weight: bold; font-size:10px;'>Investment Goal</span><br>
                <span style='color: black; font-weight: bold;'>{Inv_goal}</span>
            </div>
        """, unsafe_allow_html=True)


        # Risk Tolerance 박스
        st.markdown(f"""
            <div style="background-color:rgb(247, 251, 253); padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid gray;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <img src= "data:image/png;base64,{img_base642}" alt="image" style="width:20px; height:20px; vertical-align: middle; margin-right: 10px;">    
                <span style='color: gray; font-weight: bold; font-size:10px;'>Risk Tolerance</span><br>
                <span style='color: black; font-weight: bold;'>{Risk}</span>
            </div>
        """, unsafe_allow_html=True)

        # Investment Horizon 박스
        st.markdown(f"""
            <div style="background-color:rgb(247, 251, 253); padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid gray;box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);">
                <img src= "data:image/png;base64,{img_base643}" alt="image" style="width:20px; height:20px; vertical-align: middle; margin-right: 10px;">
                <span style='color: gray; font-weight: bold; font-size:10px;'>Investment Horizon</span><br>
                <span style='color: black; font-weight: bold;'>{inv_horizon}</span>
            </div>
        """, unsafe_allow_html=True)

        
        st.markdown(f"""
            <div style="background-color:rgb(245, 248, 251); padding: 10px; margin-bottom: 5px; border-radius: 5px; border: 1px solid gray; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <span style='color: black; font-weight: bold; font-size:20px;'>Investor Profile</span><br>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <!-- 첫 번째 박스 -->
                    <div style="background-color: #F9FBFC; padding: 10px; border-radius: 5px; border: 1px solid gray;">
                        <span style='color: gray; font-weight: bold; font-size:15px;'>Age</span><br>
                        <span style='color: black; font-weight: bold;'>{age}</span>
                    </div>
                    <!-- 두 번째 박스 -->
                    <div style="background-color:#F9FBFC; padding: 10px; border-radius: 5px; border: 1px solid gray;">
                        <span style='color: gray; font-weight: bold; font-size:15px;'>Generation</span><br>
                        <span style='color: black; font-weight: bold;'>{gen}</span>
                    </div>
                    <!-- 세 번째 박스 -->
                    <div style="background-color:#F9FBFC; padding: 10px; border-radius: 5px; border: 1px solid gray;">
                        <span style='color: gray; font-weight: bold; font-size:15px;'>Investment Horizon</span><br>
                        <span style='color: black; font-weight: bold;'>{life}</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        recommended_funds = recommend
        #st.write(recommended_funds)
        one_year_return = round(recommended_funds['oneyear'].values[0]*100, 2)
        st.markdown(f"""
            <div style="background-color:rgb(245, 248, 251); padding: 20px; margin-top: 5px; margin-bottom: 5px; border-radius: 10px; border: 1px solid #E2E8F0; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <span style='color: black; font-weight: bold; font-size:20px;'>Recommended Theme Funds</span>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-top: 15px;">
                    <div style="background-color: #FFFFFF; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0;">
                        <div style='color: #64748B; font-weight: 600; font-size:13px; margin-bottom: 5px;'>ISIN CODE</div>
                        <div style='color: #1E293B; font-weight: bold; font-size:16px;'>{recommended_funds['isin_code'].values[0]}</div>
                    </div>
                    <div style="background-color: #FFFFFF; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0;">
                        <div style='color: #64748B; font-weight: 600; font-size:13px; margin-bottom: 5px;'>LATEST NAV</div>
                        <div style='color: #1E293B; font-weight: bold; font-size:16px;'>{recommended_funds['latest_nav'].values[0]}</div>
                    </div>
                    <div style="background-color: #FFFFFF; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0;">
                        <div style='color: #64748B; font-weight: 600; font-size:13px; margin-bottom: 5px;'>1Y RETURN</div>
                        <div style='color: #2563EB; font-weight: bold; font-size:16px;'>+{one_year_return}%</div>
                    </div>
                    <div style="background-color: #FFFFFF; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0;">
                        <div style='color: #64748B; font-weight: 600; font-size:13px; margin-bottom: 5px;'>STOCK ALLOCATION</div>
                        <div style='color: #2563EB; font-weight: bold; font-size:16px;'>{int(recommended_funds['saham'].values[0])}%</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        
        # Recommendation Summary 섹션
        text = f"""Based on your profile as a {value['age']}-year-old investor in your {value['life']} stage with {value['Inv_goal']} investment objectives, we have analyzed your investment preferences and goals.

        Your {value['Risk']} risk tolerance profile, combined with an investment horizon of {value['inv_horizon']} years, aligns well with our recommended fund {recommended_funds['isin_code'].values[0]}. This fund maintains a {str(int(recommended_funds['saham'].values[0]))}% equity allocation and has demonstrated a one-year return of {round(recommended_funds['oneyear'].values[0]*100, 2)}%.

        The fund's portfolio composition and investment strategy effectively matches your {value['Risk']} approach and {value['Inv_goal']} objectives, particularly considering your current {value['life']} stage.

        This recommendation is carefully tailored to your investment preferences, {value['inv_horizon']}-year investment horizon, and life stage circumstances, providing a balanced approach to help achieve your financial goals."""

        st.markdown(f"""
            <div style="background-color:#EDF6FF; padding: 10px; margin-top: 5px; margin-bottom:5px; border-radius: 5px; border: 1px solid gray;">
                <span style='color: black; font-weight: bold; font-size:20px;'>Recommendation Summary</span><br>
                <span>{text}</span>
            </div>
        """, unsafe_allow_html=True)



    
        plot_nav_for_recommended_funds(recommended_funds)







