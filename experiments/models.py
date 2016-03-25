from django.db import models

class KeyCode(models.Model):
    key = models.CharField(max_length=255)
    code = models.IntegerField()

    def __unicode__(self):
        return "<{}>: {}".format(self.key, self.code)

class AbstractJSPsychPlugin(models.Model):

    # globally available parameters
    timing_post_trial = models.FloatField(
        help_text='Sets the time in milliseconds, \
        between the current trial and the next trial',
        default=1000)
    on_finish = models.TextField(
        help_text='A callback function to execute \
        when the trial finishes. The function is going \
        to be eval\'d at runtime so be careful before using this.')

    class Meta:
        abstract = True



class JSPsychAnimation(AbstractJSPsychPlugin):

    stimuli = models.TextField()
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
    choices = models.ManyToManyField(KeyCode)


class JSPsychText(AbstractJSPsychPlugin):
    text = models.TextField()
    cont_key = models.ManyToManyField(KeyCode)
