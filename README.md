## Text segmentation with contextual sentence surprisal

This is a novel text segmentation algorithm that takes an information-theoretic approach. It uses a concept known as surprisal (or self-information). This was written by Afrizal Hasbi Azizy (me), who took inspiration from my readings in cognitive science. It's a prototype algorithm with much work to do, but it works quite well during initial testing.

Surprisal is a value in information theory that captures the "unexpectedness" of an event. It quantifies the amount of information conveyed by an occurrence with negative log probabilities, with less probable events having higher surprisal (e.g., more "surprising").

Assume that a well-organized text can be broken down into multiple sections, each section describing unique things. The intuitive idea behind this algorithm is that the start of a new segment contains information which are new relative to both the preceding and succeeding tokens.

You can find more details in the notebook demo.

Find me: https://www.linkedin.com/in/afrizal-hasbi-azizy-182722218/

p.s. The term 'contextual' surprisal is a bit misleading, but it's the nicest-sounding placeholder name I can think of right now
