from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from analysis import analyze

# poem = """
# Last night I had a dream
# About a color that no one has seen.
# I try to explain it -- alas, in vain.
# But I have to do this or I'll go insane!

# I try to draw it but nothing comes out.
# I would write a poem but where do I start?
# The color wheel can only offer so much.
# What is there to do when there's no color of such?

# Running in circles, a usual theme --
# Looking for words to expound a dream.
# Trying for nothing, a pitiful scene:
# Describing a color that no one has seen.
# """

# analyze("A horse a horse my kingdom for a horse")

app = FastAPI()

class Poem(BaseModel):
    text: str

class AnalysisResult(BaseModel):
    rating: str
    meter: str
    rhyme_scheme: List[List[List[str]]]

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_poem(poem: Poem):
    rating = "ur poem wack bozo skill issue fr"
    meter = "foo bar"
    rhyme_scheme = analyze(poem.text)

    return AnalysisResult(
        rating=rating,
        meter=meter,
        rhyme_scheme=rhyme_scheme
    )
