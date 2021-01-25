import altair as alt
import pandas as pd
import streamlit as st

st.write("""
# Simple DNA Sequence(Nucleotide) Count Visualize App 
""")
st.header('Enter DNA sequence')

# input DNA sequence

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area("Sequence input", sequence_input, height=200)
sequence = ''.join(sequence.splitlines()[1:])


st.header("Input DNA Sequence query")
# st.markdown(sequence)
st.text(sequence)
st.header('OUTPUT (DNA Nucleotide Count)')

seq_dict = {
    'A': sequence.count('A'),
    'G': sequence.count('G'),
    'C': sequence.count('C'),
    'T': sequence.count('T'),
}

seq_df = pd.DataFrame(seq_dict.items())
seq_df.columns = ['nucleotide', 'count']

st.subheader('DNA Sequence Count')
st.write('There are  ' + str(seq_dict['A']) + ' adenine (A)')
st.write('There are  ' + str(seq_dict['T']) + ' thymine (T)')
st.write('There are  ' + str(seq_dict['G']) + ' guanine (G)')
st.write('There are  ' + str(seq_dict['C']) + ' cytosine (C)')


# DNA Sequence Dataset

st.subheader('DNA Sequence Dataset')
st.write(seq_df)

st.subheader("""
DNA count Bar Chart
""")

p = alt.Chart(seq_df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(60)  
)
st.write(p)