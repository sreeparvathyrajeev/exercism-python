"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    return (
        temperature < 800 and
        neutrons_emitted > 500 and
        temperature * neutrons_emitted < 500000
    )
    

    


def reactor_efficiency(voltage, current, theoretical_max_power):
    if ((voltage*current)/theoretical_max_power)*100 >= 80:
        efficiency='green'
    elif 60 <= ((voltage*current)/theoretical_max_power)*100 <80:
        efficiency='orange'
    elif 30 <= ((voltage*current)/theoretical_max_power)*100 < 60:
        efficiency='red'
    else:
        efficiency='black'
    return efficiency

    

    

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature*neutrons_produced_per_second) < (0.9*threshold):
        status='LOW'
    elif (0.9*threshold) <= (temperature*neutrons_produced_per_second) <= (1.1*threshold):
        status='NORMAL'
    else:
        status='DANGER'
    return status