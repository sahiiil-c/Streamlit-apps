import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title="Ashu's saloon", page_icon="new logo.png", layout="centered")
def get_base64(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("new logo.png")
# st.title("Ashu's Makeover",text_alignment="center")
#====================================================================================
# Display the logo at the top of the page, centered, with a height of 200px
#====================================================================================#
st.markdown(f"""
    <div style="display:flex; justify-content:center; ">
        <img src="data:image/png;base64,{img}" height="150px" alt="Logo">
    </div>
    
""", unsafe_allow_html=True)

#====================================================================================
# Set the background of the entire app to a gradient from #1e3c72 to #2a5298 to skyblue, with a diagonal direction (315 degrees)
#====================================================================================
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(315deg, #1e3c72, #2a5298,skyblue);
            background-attachment: flex;
            background-size: cover;
            
        }
    </style>
""", unsafe_allow_html=True)


# hide the streamlit menu and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


#===========================
# Start app function
#===========================

def start_app(path):
    import firebase_admin
    from firebase_admin import credentials, firestore
    
    path = dict(path)
    
    # Fix newline issue
    path['private_key'] = path['private_key'].replace('\\n', '\n')
    
    # Initialize only once
    if not firebase_admin._apps:
        cred = credentials.Certificate(path)
        firebase_admin.initialize_app(cred)
        
    return firestore.client()

# function to get document list for specific data 

def get_doc_data(_db,collection_name:str,doc_name:str):
    doc_d =_db.collection(collection_name).document(doc_name).get().to_dict()
    return doc_d

# make Clean table for representation

def represent_df(db,order:list,set_index:str):
    import pandas as pd

    actual=list(db.keys())
    if all(key in actual for key in order):
        if type(db[actual[0]])==list:
            df=pd.DataFrame(db,columns=order)
            df[set_index]=df[set_index].str.capitalize()
            df.columns=df.columns.str.capitalize().str.replace("_"," ")
            df=df.set_index(set_index.capitalize())
        
        else:
            df=pd.DataFrame(db,index=[0],columns=order)
            df[set_index]=df[set_index].str.capitalize()
            df.columns=df.columns.str.capitalize().str.replace("_"," ")
            df=df.set_index(set_index.capitalize())

        return df
    else:
        st.error("incorrect order")




# Correct way to access secrets
db = start_app(st.secrets["firebase"])

# if db:
#     st.success("db connected succesfully🚀")

st.markdown(
    "<h6 style='color: #D4AF37;'>Mobile no. - 8652200634</h6>",
    unsafe_allow_html=True
)

hair,face,body,feet = st.tabs(["💇‍♀️ Hair Lounge","🌸 Skin Studio","🌿 Body Rituals","👣 Foot Therapy Spa"])


with hair:
    
    hair_db = get_doc_data(db,"service","hair")

    if not hair_db:
        st.error("⚠️ Hair document is empty or not found")
        st.stop()
    
    
    chem_treat= hair_db['chemical_treatment']
    hair_spa= hair_db['hair_spa']
    hair_cut= hair_db['hair_cut']
    hair_styling=hair_db['hair_styling']
    
    
    chem_t,haircut_t,hairspa_t,hairstyle_t = st.tabs(['💇‍♀️ Hair Transformations','✂️ Precision Cuts',"💆‍♀️ Hair Therapy","🎨 Style & Finish"])
    
    with chem_t:
        # st.write(chem_treat['service'][0])

        st.table(represent_df(chem_treat,order=['service','short','medium','long'],set_index='service'),border=False)
        
    with haircut_t:
        # st.write(hair_cut['service'][0])
                
        st.table(represent_df(hair_cut,order=['service','price'],set_index='service'),border=False)
        
    with hairspa_t:
        hair_spa_keys = list(hair_spa.keys())
        
        st.table(represent_df(hair_spa,order=['service','short',"medium","long"],set_index='service'),border=False)
        # st.table(pd.DataFrame(hair_spa,columns=["extra_ampules"],index=[0]).)
        hairspa_col1,hairspa_col2,hairspa_col3,hairspa_col4 = st.columns(4,gap="xxsmall")
                    
        with hairspa_col1:
            
            
            st.table(pd.DataFrame(hair_spa,columns=["extra_ampules"],index=[0]).T.rename(columns={0:"Price"}),border=False)
            
             
    with hairstyle_t:
        
        
        
        st.table(represent_df(hair_styling,order=['service','price'],set_index='service'),border=False)

with face:
    face_db = get_doc_data(db,"service","face")
    # emojis to the tabs below
    
    face_col1,face_col2,face_col3,face_col4,face_col5,face_col6 = st.tabs(["🍯 Face waxing","🧵 Thread & Shape","✨ Bleach","🧼 Quick Glow","🧖‍♀️ Facials","🌞 Tan Removal"])
    
    #==============================================================================
    
    with face_col1:
        st.table(represent_df(face_db['face_wax'],order=['service','price'],set_index='service'),border=False)
    
    with face_col2:
        
        
        st.table(represent_df(face_db['threading'],order=['service','price'],set_index='service'),border=False)
    
    with face_col3:
        
        st.table(represent_df(face_db['bleach'],order=['service','price'],set_index='service'),border=False)
    
    with face_col4:
        
        
        st.table(represent_df(face_db['clean_up'],order=['service','price'],set_index='service'),border=False)
    
    with face_col5:
        
        
        st.table(represent_df(face_db['facials'],order=['service','price'],set_index='service'),border=False)
        
    with face_col6:
        
        
        st.table(represent_df(face_db['dtan'],order=['service','price'],set_index='service'),border=False)
    
    
    
    
    #==============================================================================    

#==============================================================================


with body:
    body_db = get_doc_data(db,"service","body")
    
    
    body_col1,body_col2,body_col3,body_col4 = st.tabs(["🍯 Body Waxing","⚪ Skin Lightening","✨ Body Polishing","🌞 Tan Removal Ritual"])
    
    with body_col1:
        st.table(represent_df(body_db['waxing'],order=['service','price'],set_index='service'),border=False)
        
    with body_col2:
        st.table(represent_df(body_db['bleach'],order=['service','price'],set_index='service'),border=False)
    
    with body_col3:
        st.table(represent_df(body_db['polishing'],order=['service','price'],set_index='service'),border=False)
    
    with body_col4:
        st.table(represent_df(body_db['dtan'],order=['service','price'],set_index='service'),border=False)

    
with feet:
    feet_db = get_doc_data(db,"service","feet")
    
    # make 2 tabs for feet bleach and dtan
    feet_col1,feet_col2 = st.tabs(["⚪ Foot Brightening","🌞 Foot Tan Removal"])
    
    with feet_col1:
        feet_dtan_df=represent_df(feet_db['dtan'],order=['service','price'],set_index='service')
        feet_dtan_df.reset_index(inplace=True)
        feet_dtan_df['Service']="Foot Brightening"
        st.table(feet_dtan_df.set_index('Service'),border=False)
    
    with feet_col2:
        feet_dtan_df=represent_df(feet_db['dtan'],order=['service','price'],set_index='service')
        feet_dtan_df.reset_index(inplace=True)
        feet_dtan_df['Service']="Foot Tan Removal"
        st.table(feet_dtan_df.set_index('Service'),border=False)
    
