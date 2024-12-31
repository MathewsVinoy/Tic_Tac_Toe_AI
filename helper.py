import matplotlib.pyplot as plt
from IPython import display

plt.ion()  # Enable interactive mode

def plot(score, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(score, label='Score')
    plt.plot(mean_scores, label='Mean Score')
    plt.ylim(ymin=0)
    plt.legend()
    plt.text(len(score)-1, score[-1], str(score[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.draw()  # Ensure the plot is drawn
    plt.pause(0.01)  # Pause to allow the plot to update

