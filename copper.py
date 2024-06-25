import streamlit as st
import numpy as np
import re

# Placeholder function to simulate model training (selling price prediction)
def train_sell_model(X_train, y_train):
    # Replace with actual model training code
    return None

# Placeholder function to simulate model training (status prediction)
def train_status_model(X_train, y_train):
    # Replace with actual model training code
    return None

# Placeholder function to simulate model prediction for selling price
def predict_sell_price(sample):
    # Replace with actual model prediction code
    return np.random.randint(1000, 5000)

# Placeholder function to simulate model prediction for status
def predict_status(sample):
    # Replace with actual model prediction code
    return np.random.choice([0, 1])

# Streamlit UI
st.write("""

    Industrial Copper Modeling Application

""", unsafe_allow_html=True)

# Tabs for different functionalities
tab1, tab2 = st.columns(2)
with tab1:
    st.write("## PREDICT SELLING PRICE")
    status_options = ['Won', 'Draft', 'to be approved', 'lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered',
                      'Offerable']
    item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
    country_options = [28., 25., 30., 32., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
    application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67.,
                           79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
    product = ['611993', '611728', '628112', '628117', '628377', '640400', '640405', '640665','611993', '929423819',
               '1282007633', '1332077137', '164141591', '164336407',
               '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662',
               '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738',
               '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']

    with st.form('my_form'):
        col1, col2, col3 = st.columns([5, 2, 5])
        with col1:
            st.write(' ')
            status = st.selectbox('Status', status_options, key=1)
            item_type = st.selectbox('Item Type', item_type_options, key=2)
            country = st.selectbox('Country', sorted(country_options), key=3)
            application = st.selectbox('Application', sorted(application_options), key=4)
            product_ref = st.selectbox('Product Reference', product, key=5)
        with col3:
            quantity_tons = st.text_input('Enter Quantity Tons (Min:611728 & Max:1722207579)')
            thickness = st.text_input('Enter thickness (Min:0.18 & Max:400)')
            width = st.text_input('Enter width(Min:1, Max:2990)')
            customer = st.text_input('customer ID (Min:12458, Max:30408185)')
            submit_button = st.form_submit_button(label='Predict Selling Price')
            st.markdown('''
            ''', unsafe_allow_html=True)

        flag = 0
        pattern = '^(?:\d+|\d*\.\d+)$'
        for i in [quantity_tons, thickness, width, customer]:
            if re.match(pattern, i):
                pass
            else:
                flag = 1
                break

    if submit_button and flag == 1:
        if len(i) == 0:
            st.write('please enter a valid number space not allowed')
        else:
            st.write('you have entered an invalid value: ', i)

    if submit_button and flag == 0:
        # Placeholder for model prediction
        sample = np.array([[np.log(float(quantity_tons)), application, np.log(float(thickness)), float(width),
                            country, float(customer), int(product_ref), item_type, status]])
        new_pred = predict_sell_price(sample)
        st.write('## :green[Predicted selling price:] ', np.exp(new_pred))

with tab2:
    st.write("## PREDICT STATUS")
    with st.form('my_form1'):
        col1, col2, col3 = st.columns([5, 1, 5])
        with col1:
            cquantity_tons = st.text_input('Enter Quantity Tons (Min:611728 & Max:1722207579)')
            cthickness = st.text_input('Enter thickness (Min:0.18 & Max:400)')
            cwidth = st.text_input('Enter width (Min:1, Max:2990)')
            ccustomer = st.text_input('customer ID (Min:12458, Max:30408185)')
            cselling = st.text_input("Selling Price (Min:1, Max:100001015)")

        with col3:
            st.write(' ')
            citem_type = st.selectbox("Item Type", item_type_options, key=21)
            ccountry = st.selectbox("Country", sorted(country_options), key=31)
            capplication = st.selectbox("Application", sorted(application_options), key=41)
            cproduct_ref = st.selectbox("Product Reference", product, key=51)
            csubmit_button = st.form_submit_button(label="PREDICT STATUS")

        cflag = 0
        pattern = "^(?:\d+|\d*\.\d+)$"
        for k in [cquantity_tons, cthickness, cwidth, ccustomer, cselling]:
            if re.match(pattern, k):
                pass
            else:
                cflag = 1
                break

    if csubmit_button and cflag == 1:
        if len(k) == 0:
            st.write("please enter a valid number space not allowed")
        else:
            st.write("You have entered an invalid value: ", k)

    if csubmit_button and cflag == 0:
        # Placeholder for model prediction
        sample = np.array([[np.log(float(cquantity_tons)), np.log(float(cselling)), capplication,
                            np.log(float(cthickness)), float(cwidth), ccountry, int(ccustomer), int(cproduct_ref),
                            citem_type]])
        new_pred = predict_status(sample)
        if new_pred == 1:
            st.write('## :green[The Status is Won] ')
        else:
            st.write('## :red[The status is Lost] ')
