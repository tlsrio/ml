from transformers import pipeline
import json

ARTICLE = """Indian billionaires increased their wealth by 35% during the lockdown to ₹ 3 trillion, ranking India 
after U.S., China, Germany, Russia and France. Out of these, the rise in fortunes for the top 100 billionaires since 
the lockdown in March is enough to give every one of the 138 million poorest Indian people a cheque for ₹94,045 each, 
according to Oxfam’s ‘Inequality Virus Report’ released on the opening day of the World Economic Forum in Davos. The 
wealth of just the top 11 billionaires during the pandemic could easily sustain the MGNREGS or the Health Ministry 
for the next 10 years, stated the report, which underscored the deepening inequalities due to COVID-19 where the 
wealthiest escaped the worst impact of the pandemic while the poor faced joblessness, starvation and death. Mukesh 
Ambani, who emerged as the richest man in India and Asia, earned ₹90 crore an hour during the pandemic when around 
24% of the people in the country were earning under ₹ 3,000 a month during the lockdown. The increase in his wealth 
alone could keep 40 crore informal workers out of poverty for at least five months, said the report.It recommended 
reintroducing the wealth tax and effecting a one-time COVID-19 cess of 4% on taxable income of over ₹10 lakh to help 
the economy recover from the lockdown. According to its estimate, wealth tax on the nation’s 954 richest families 
could raise the equivalent of 1% of the GDP. The report also delved deeper into different forms of inequities, 
including educational, gender and health, which meant that facilities to wash hands and maintain distance, 
essential to prevent the spread of Coronavirus, was impossible for a majority of the population. According to the 
report, only 6% of the poorest 20% have access to non-shared sources of improved sanitation, compared to 93.4 % of 
the top 20 %. 59.6 % of India’s population lived in a room or less, which meant that protocols necessary to prevent 
the spread of COVID-19 cannot be followed. While the government took steps to make COVID-19 services affordable by 
including them under Ayushman Bharat-PMJAY, the scheme only covered BPL (below poverty line) population leaving out 
the uninsured poor and the middle class. Till October, 32 crores students were hit by closure of schools, of whom 84 
% resided in rural areas and 70 %attended government schools. Oxfam India’s survey across five States said that close 
to 40 % of teachers in government schools feared that the prolonged school closure might lead to a third of the 
students not returning once schools reopened. It was estimated that out of school rates would double in a year. 
Dalits, Adivasis and Muslims were likely to see a higher rate of dropout. Girls were also most vulnerable as they 
were at risk of early and forced marriage, violence and early pregnancies, it noted. Unemployment of women rose by 
15% from a pre-lockdown level of 18 %, which could result in a loss of India’s GDP of about 8 % or ₹15 trillion. 
Women who were employed before the lockdown were also 23.5 percentage points less likely to be re-employed compared 
to men in the post lockdown phase. """


def getNER(sequence):
    nlp = pipeline("ner")

    result = nlp(sequence)
    # res = classifier(text, categories, multi_class=True)
    # res = {res['labels'][i]: res['scores'][i] for i in range(len(res['labels']))}
    # res = json.dumps(res)
    return result


print(getNER(ARTICLE))
