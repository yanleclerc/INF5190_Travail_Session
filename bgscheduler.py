"""
 Copyright 2021 Ela El-Heni
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

#A3
#BackgroundScheduler pour telecharger les données de la ville chaque jour à minuit
#Ce bout de code peut etre deplacé à votre guise, faire attention aux imports circulaires

#pip3 install appscheduler
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import manage

#set scheduler
sched = BackgroundScheduler(daemon=True)
sched.add_job(manage.data_handler(),'cron',hour=0)
sched.start()
atexit.register(lambda: sched.shutdown())