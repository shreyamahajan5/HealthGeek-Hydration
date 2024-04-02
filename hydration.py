import streamlit as st
import datetime

def calculate_hydration_needs(weight, activity_level, gender, exercise, environment, overall_health, pregnancy):
    # Example calculation - you can replace this with a more advanced formula
    basal_metabolic_rate = weight * 24  # Assuming a simple formula for basal metabolic rate
    hydration_needs = basal_metabolic_rate * activity_level

    # Adjust hydration needs based on gender and additional factors
    if gender == 'Male':
        hydration_needs += 3700  # 15.5 cups (3.7 liters) for men
    else:
        hydration_needs += 2700  # 11.5 cups (2.7 liters) for women

    if exercise:
        hydration_needs += 500  # Additional fluid intake for exercise

    if environment == 'Hot/Humid':
        hydration_needs += 1000  # Additional fluid intake for hot or humid weather

    if overall_health == 'Fever/Vomiting/Diarrhea':
        hydration_needs += 1000  # Additional fluid intake for fever, vomiting, or diarrhea

    if pregnancy:
        hydration_needs += 500  # Additional fluid intake for pregnancy

    return hydration_needs

def send_reminder(reminder_time):
    current_time = datetime.datetime.now().time()
    if current_time > reminder_time:
        st.warning("It's time to drink water!")
    else:
        st.info(f"Next reminder at {reminder_time}")

def generate_drinking_schedule(total_hydration_needs, num_intervals):
    interval_amount = total_hydration_needs / num_intervals
    intervals_per_day = 3  # Morning, Afternoon, Night
    interval_time = 24 / intervals_per_day
    schedule = {}
    for i in range(intervals_per_day):
        for j in range(num_intervals // intervals_per_day):
            hour = int(interval_time * i + (interval_time / (num_intervals // intervals_per_day)) * j)
            time = datetime.time(hour, 0)
            schedule[time] = interval_amount
    return schedule

def main():
    st.title('HealthGeek')

    st.markdown(
        """
        <div style='display:flex; align-items:center;'>
            <h1 style='margin-left:10px;'> Hydration Calculator</h1>
            <img src='https://tenor.com/view/mochi-drink-water-gif-26421523.gif' width='200'>
            
        </div>
        
        """,
        unsafe_allow_html=True
    )
    
    # User inputs
    weight = st.slider('Weight (kg):', min_value=20, max_value=200, value=70)
    activity_level = st.slider('Activity Level:', min_value=1, max_value=3, value=2, format='%d - Low:1, Moderate:2, High:3')
    gender = st.radio('Gender:', ['Male', 'Female'])
    exercise = st.checkbox('Do you exercise?')
    environment = st.radio('Environment:', ['Normal', 'Hot/Humid'])
    overall_health = st.radio('Overall Health:', ['Normal', 'Fever/Vomiting/Diarrhea'])
    pregnancy = st.checkbox('Are you pregnant/breastfeeding?')

    # Calculate hydration needs
    hydration_needs = calculate_hydration_needs(weight, activity_level, gender, exercise, environment, overall_health, pregnancy)

    # Display hydration needs
    st.subheader('Estimated Hydration Needs:')
    st.write(f'You should drink approximately {hydration_needs:.2f} ml of water per day.')

    # Tentative Water Drinking Schedule
    st.subheader('Tentative Water Drinking Schedule:')
    num_intervals = st.slider('Number of Drinking Intervals:', min_value=3, max_value=10, value=5)
    drinking_schedule = generate_drinking_schedule(hydration_needs, num_intervals)
    for time, amount in drinking_schedule.items():
        st.write(f"At {time.strftime('%H:%M')}: Drink {amount:.2f} ml of water.")

    # Reminder Functionality
    reminder_time = st.time_input("Set a reminder time:", datetime.time(8, 0))
    send_reminder(reminder_time)

def sidebar():
    st.sidebar.title("Stay Hydrated, Stay Healthy!")
    st.sidebar.write(
        """
        Welcome to the Interactive Hydration Calculator! Proper hydration is essential for maintaining 
        optimal health and well-being. Use this tool to calculate your daily hydration needs, create a 
        tentative water drinking schedule, track your water consumption, and receive personalized 
        recommendations to stay hydrated throughout the day.
        """
    )

    st.sidebar.subheader("Tips for Staying Hydrated:")
    st.sidebar.write(
        """
        - Drink water before you feel thirsty to prevent dehydration.
        - Carry a reusable water bottle with you to stay hydrated on-the-go.
        - Set reminders to drink water at regular intervals throughout the day.
        - Consume hydrating foods such as fruits and vegetables.
        - Avoid excessive intake of caffeinated or alcoholic beverages, as they can lead to dehydration.
        """
    )

    st.sidebar.subheader("Why Hydration Matters:")
    st.sidebar.write(
        """
        Proper hydration plays a vital role in maintaining various
        """
    )

if __name__ == "__main__":
    sidebar()
    main()
