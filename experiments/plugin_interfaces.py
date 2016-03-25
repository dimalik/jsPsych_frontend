"""

As of now the following plugins are supported
jspsych‑animation
jspsych‑button‑response
jspsych‑call‑function
jspsych‑categorize
jspsych‑categorize‑animation
jspsych‑free‑sort
jspsych‑html
jspsych‑instructions
jspsych‑multi‑stim‑multi‑response
jspsych‑palmer
jspsych‑reconstruction
jspsych‑same‑different
jspsych‑similarity
jspsych‑single‑audio
jspsych‑single‑stim
jspsych‑survey‑likert
jspsych‑survey‑multi‑choice
jspsych‑survey‑text
jspsych‑text
jspsych‑visual‑search‑circle
jspsych‑vsl‑animate‑occlusion
jspsych‑vsl‑grid‑scene
jspsych‑xab
"""

class JSPsychAnimation(AbstractJSPsychPlugin):

    stimuli = models.ManyToManyField(parameterClasses.image_path)
    frame_time = models.FloatField(
        default=250,
        help_text="How long to display each image (in milliseconds).")
    frame_isi = models.FloatField(
        default=0,
        help_text="If greater than 0, then a gap will be shown between each \
image in the sequence. This parameter specifies the length of the gap.")
    sequence_reps_time = models.IntegerField(
        default=1,
        help_text="How many times to show the entire sequence. There will be \
no gap (other than the gap specified by frame_isi) between repetitions.")
    prompt = models.CharField(max_length=255)
    choices = models.ManyToManyField(parameterClasses.keys)
