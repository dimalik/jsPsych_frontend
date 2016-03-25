from experiments.models import KeyCode


with open("experiments/keycodes.txt") as fin:
    kc = [dict(zip(['key', 'code'], x.split('\t')))
          for x in fin.read().split('\n')]

KeyCode.objects.bulk_create([KeyCode(**item)
                             for item in kc if item.get('code', '')])
