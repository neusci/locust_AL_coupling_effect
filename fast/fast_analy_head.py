# !/usr/bin/env python
# -*- coding:utf-8 -*-

#execfile("../slow/slow_analy_head.py")

def corr_coeff_between_vol_array(a, b):
    """
      a is vol array of a PN;  b is the sum of vol of all PNs
      both a and b are arrays. They have the same shape
      a and b should usually be vol between osc_begin and osc_end
    ...
      return the correlation coefficient
    ...
      a=loaddata(0,0,0)
      b=sum(a,0)[osc_begin:osc_end]
      corr_coeff(a[0,osc_begin:osc_end], b)
      plot(a[0,osc_begin:osc_end], b, '.'); show()
      plot(a[0,osc_begin:osc_end]+65); plot(b/1000+48); show()
      # the above curves are adjusted to make them nearer with eachother
    """
    # eliminate effects of spikes
    a_tmp = zeros(shape(a))
    a_tmp[:] = a[:]
    a_tmp[a_tmp > -50] = -50
    #  http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.linregress.html
    slope, intercept, r_value, p_value, std_err = stats.linregress(a_tmp, b)
    return r_value

"""  # an example of using corr_coeff (with count_spike_number_in_vol_list)
# this is used to calculate the avg correlation coefficience of PNs at 0,1,... spikes in [osc_being, osc_end]
a = loaddata(0,0,0)
b = sum(a,0)[osc_begin:osc_end]
binpos = [ [ count_spike_number_in_vol_list(a[i, osc_begin:osc_end]), abs(corr_coeff(a[i,osc_begin:osc_end],b)) ] for i in range(PN_number) ]
binpos = array(binpos)
plot(binpos[:,0], binpos[:,1], '.')

avg_bp=zeros(20)
num_bp=zeros(20)
for i in rlen(binpos):
    num_bp[ binpos[i,0] ] += 1
    avg_bp[ binpos[i,0] ] += binpos[i,1]

for i in rlen(num_bp):
    if num_bp[i] <= 0: continue
    avg_bp[i] /= num_bp[i]

plot(avg_bp[:12])
xlabel("spike number")
ylabel("abs(corr_coeff)")
savefig("binpos.jpg")
show()
"""


def corr_coeff_array_from_vol_matrix(a, tbgn, tend):
    """
      a is vol matrix of all PNs
      tbgn and tend define the time range, usually between osc_begin and osc_end
    ...
      return an array of the correlation coefficient of all PNs
    ...  Example:
       x=load_sf_avged_over_trial(0,0,1500,3500)
       y0=corr_coeff_array_from_vol_matrix(loaddata(0,0,0), 1500, 3500)
       y1=corr_coeff_array_from_vol_matrix(loaddata(0,0,1), 1500, 3500)
       y2=corr_coeff_array_from_vol_matrix(loaddata(0,0,2), 1500, 3500)
       y3=corr_coeff_array_from_vol_matrix(loaddata(0,0,3), 1500, 3500)
       y4=corr_coeff_array_from_vol_matrix(loaddata(0,0,4), 1500, 3500)
       plot(x,(y0+y1+y2+y3+y4)/5.0,'.')
       show()
    """
    # eliminate effects of spikes
    a_tmp = zeros([PN_number, tend-tbgn])
    a_tmp[:] = a[:,tbgn:tend]
    a_sum=sum(a_tmp, 0)
    a_tmp[a_tmp > -50] = -50
    #  http://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.linregress.html
    r_arr=zeros(PN_number)
    for i in range(PN_number):
        slope, intercept, r_value, p_value, std_err = stats.linregress(a_tmp[i], a_sum)
        r_arr[i] = r_value
    return r_arr
