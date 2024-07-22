import streamlit as st

# Define updated emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.12,  # kgCO2/km (Updated value)
        "Electricity": 0.73,  # kgCO2/kWh (Updated value)
        "Digital_Devices": 0.03,  # kgCO2/kWh for digital devices (example value)
        "Internet_Usage": 0.05  # kgCO2/GB for internet data usage (example value)
    }
}

# Set wide layout and page title
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Streamlit app code
st.title("🌱 Personal Carbon Footprint Calculator")

# Sidebar for inputs
st.sidebar.header("Input Details")

# User inputs in the sidebar
country = st.sidebar.selectbox("Select Your Country", ["India"])

st.sidebar.subheader("Daily Commute")
distance = st.sidebar.slider("Commute Distance (in km)", 0.0, 100.0, 0.0)

st.sidebar.subheader("Electricity Usage")
electricity = st.sidebar.slider("Monthly Electricity Consumption (in kWh)", 0.0, 1000.0, 0.0)

st.sidebar.subheader("Digital Activities")
screen_time = st.sidebar.slider("Daily Screen Time (in hours)", 0.0, 24.0, 0.0)
internet_usage = st.sidebar.slider("Daily Internet Usage (in GB)", 0.0, 50.0, 0.0)

# Normalize inputs
distance *= 365  # Convert daily distance to yearly
electricity *= 12  # Convert monthly electricity to yearly
screen_time *= 365  # Convert daily screen time to yearly
internet_usage *= 365  # Convert daily internet usage to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
digital_devices_emissions = EMISSION_FACTORS[country]["Digital_Devices"] * (screen_time * 0.5)  # Assuming average consumption per hour
internet_emissions = EMISSION_FACTORS[country]["Internet_Usage"] * internet_usage

# Convert emissions to tonnes and round to 2 decimal places
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
digital_devices_emissions = round(digital_devices_emissions / 1000, 2)
internet_emissions = round(internet_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + digital_devices_emissions + internet_emissions, 2
)

# Display results
if st.sidebar.button("Calculate CO2 Emissions"):

    st.subheader("📊 Carbon Emissions Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="🚗 Transportation", value=f"{transportation_emissions} tonnes CO2/year")
        st.metric(label="💡 Electricity", value=f"{electricity_emissions} tonnes CO2/year")
        st.metric(label="💻 Digital Devices", value=f"{digital_devices_emissions} tonnes CO2/year")
        st.metric(label="🌐 Internet Usage", value=f"{internet_emissions} tonnes CO2/year")

    with col2:
        st.metric(label="🌍 Total Carbon Footprint", value=f"{total_emissions} tonnes CO2/year")
        st.info("As of 2024, the average CO2 emissions per capita in India is approximately 2.0 tons. Since 1972, emissions have increased significantly from 0.39 tons to 2.0 tons annually.")

    st.markdown("---")
    st.markdown("### Strategies for Reducing Your Carbon Footprint")
    st.write(
        """
        - **Transportation:** Opt for public transportation, carpooling, or electric vehicles to reduce emissions.
        - **Electricity:** Upgrade to energy-efficient appliances and consider renewable energy sources.
        - **Digital Activities:** Reduce screen time, use energy-efficient devices, and optimize internet usage to lower digital emissions.
        """
    )
