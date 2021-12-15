""" Meltdown Mitigation exercise """


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    product = temperature * neutrons_emitted 
    if temperature < 800 and neutrons_emitted  > 500 and product < 500000:
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: voltage value (integer or float)
    :param current: current value (integer or float)
    :param theoretical_max_power: power that corresponds to a 100% efficiency (integer or float)
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power = voltage * current
    percent_value = (generated_power / theoretical_max_power)*100
    perc_value = int(percent_value)
    if perc_value >= 80:
        return 'green'
    elif perc_value < 80 and perc_value >= 60:
        return 'orange'
    elif perc_value < 60 and perc_value >= 30:
        return 'red'
    elif perc_value < 30:
        return 'black'
    
    


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: value of the temperature (integer or float)
    :param neutrons_produced_per_second: neutron flux (integer or float)
    :param threshold: threshold (integer or float)
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 90% of `threshold` == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutrons per second` is not in the above-stated ranges ==  'DANGER'
    """
    
    reactor_val = (temperature * neutrons_produced_per_second)
    th_val = threshold
    ten_percent = (th_val * 0.10)
    ninety_percent = th_val - ten_percent
    hundred_and_ten_percent = th_val + ten_percent
    
    #If the reactor_value is < 90% of the threshold - return LOW
    if reactor_val < (th_val * 0.90):
        return 'LOW'
    #If the relactor value is between 110% and 90% of the threshold - return NORMAL
    elif reactor_val <= hundred_and_ten_percent and reactor_val >= ninety_percent:
        return 'NORMAL'
    #Otherwise, return DANGER
    else:
        return 'DANGER'
    
    
    
