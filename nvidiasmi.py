#!/usr/bin/env python
# coding: utf-8

# In[127]:


from plumbum.cmd import nvidia_smi
from datadog_checks.checks import AgentCheck


# In[128]:


class sensor(AgentCheck):
    def check(self, instance):
        a=nvidia_smi["--query-gpu=timestamp,temperature.gpu,memory.used,memory.total,fan.speed,utilization.gpu","--format=csv"]
        a=a()
        a=a.encode("utf-8")
        a=a.split(",")
        print(a)
        
        temp=int(a[6])
        mem_used=a[7].split()
        mem_used=int(mem_used[0])
        mem_total=a[8].split()
        mem_total=int(mem_total[0])
        fan_speed=a[9].split()
        fan_speed=int(fan_speed[0])


        gpu_load=a[10].split()
        try:
            gpu_load = int(gpu_load[0])
        except:
            gpu_load =0



        
        self.gauge('nvidia_smi.temp',temp)
        self.gauge('nvidia_smi.mem_used',mem_used)
        self.gauge('nvidia_smi.mem_total',mem_total)
        self.gauge('nvidia_smi.fan_speed',fan_speed)
        self.gauge('nvidia_smi.gpu_load',gpu_load)

