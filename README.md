# ArtifactThoughts
dummy_data.py generates two computers playing a drafting game similar to Artifact. (four colors, strength 0 -> 9, score is a sum of the strengths minus how many of your cards are countered B > G > R > U > B ...)

classifier.py is a super simple decision tree regressor to calculate probability of winning at each board state.

ask_gaben.py puts it all together where given a board state (two hands and four cards to choose from) it uses the classifier to predict the probability of winning each of the four choices, then chooses the highest.

I think where I go from here is to try to generate an image/video scraper to pull drafting data, then actually tune the model and try a couple different approaches, then figure out a cleaner ui for entering and displaying the optimal choice.
