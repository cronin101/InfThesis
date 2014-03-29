import sys
import csv
import pyparsing

import matplotlib
import matplotlib.backends.backend_pdf

from pylab import *


task_directory = sys.argv[1]
task_description = '[' + sys.argv[2] + '] '

show_bespoke = True
if len(sys.argv) == 4:
    show_bespoke = False

def get_list_from_file(filename, form=float):
    with open(task_directory + '/' + filename, 'rb') as f:
        fr = csv.reader(f, delimiter=',')
        return [form(n) for row in fr for n in row]

input_sizes = get_list_from_file('input_sizes.csv', form=int)

vanilla_ruby_laptop = get_list_from_file('laptop/v_ruby.csv')
rubicl_cpu_laptop = get_list_from_file('laptop/cpu.csv')
rubicl_gpu_laptop = get_list_from_file('laptop/gpu.csv')

if show_bespoke:
    bespoke_ruby_laptop = get_list_from_file('laptop/bespoke.csv')
    bespoke_ruby_pc = get_list_from_file('pc/bespoke.csv')

vanilla_ruby_pc = get_list_from_file('pc/v_ruby.csv')
rubicl_cpu_pc = get_list_from_file('pc/cpu.csv')
rubicl_gpu_pc = get_list_from_file('pc/gpu.csv')

plot(input_sizes, vanilla_ruby_laptop, linestyle='-', marker='o', markersize=4, color='r',
        label="Vanilla Ruby (Laptop)")
plot(input_sizes, rubicl_cpu_laptop, linestyle='-', marker='o', markersize=4, color='b',
        label="RubiCL on CPU (Laptop)")
plot(input_sizes, rubicl_gpu_laptop, linestyle='-', marker='o', markersize=4, color='g',
        label="RubiCL on GPU (Laptop)")

if show_bespoke:
    plot(input_sizes, bespoke_ruby_laptop, linestyle='-', marker='o', markersize=4, color='k',
            label="Bespoke C Extension (Laptop)")
    plot(input_sizes, bespoke_ruby_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='k',
            label="Bespoke C Extension (PC)")


plot(input_sizes, vanilla_ruby_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='r',
        label="Vanilla Ruby (PC)")
plot(input_sizes, rubicl_cpu_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='b',
        label="RubiCL on CPU (PC)")
plot(input_sizes, rubicl_gpu_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='g',
        label="RubiCL on GPU (PC)")

xlabel('Dataset size (elements)', fontsize=8)
ylabel('Runtime (seconds)', fontsize=8)
#ylim([0, max(vanilla_ruby_laptop)])
legend(framealpha=0.2, prop={'size':8}, loc='best')
title(task_description + 'Duration by execution target', fontsize=8)
savefig(task_directory + '/runtimes.pdf', bbox_inches='tight')
show()

# percentage of vanilla performance
cpu_vp_laptop = [ v / x for (v, x) in zip(vanilla_ruby_laptop, rubicl_cpu_laptop)]
gpu_vp_laptop = [ v / x for (v, x) in zip(vanilla_ruby_laptop, rubicl_gpu_laptop)]

if show_bespoke:
    bespoke_vp_laptop = [ v / x for (v, x) in zip(vanilla_ruby_laptop, bespoke_ruby_laptop)]
    bespoke_vp_pc = [ v / x for (v, x) in zip(vanilla_ruby_pc, bespoke_ruby_pc)]

cpu_vp_pc = [ v / x for (v, x) in zip(vanilla_ruby_pc, rubicl_cpu_pc)]
gpu_vp_pc = [ v / x for (v, x) in zip(vanilla_ruby_pc, rubicl_gpu_pc)]

plot(input_sizes, cpu_vp_laptop, linestyle='-', marker='o', markersize=4, color='b',
        label="RubiCL on CPU (Laptop)")
plot(input_sizes, gpu_vp_laptop, linestyle='-', marker='o', markersize=4, color='g',
        label="RubiCL on GPU (Laptop)")

if show_bespoke:
    plot(input_sizes, bespoke_vp_laptop, linestyle='-', marker='o', markersize=4, color='k',
            label="Bespoke C Extension (Laptop)")
    plot(input_sizes, bespoke_vp_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='k',
            label="Bespoke C extension (PC)")

plot(input_sizes, cpu_vp_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='b',
        label="RubiCL on CPU (PC)")
plot(input_sizes, gpu_vp_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='g',
        label="RubiCL on GPU (PC)")

xlabel('Dataset size (elements)', fontsize=8)
ylabel('Proportion of vanilla Ruby performance', fontsize=8)
legend(framealpha=0.2, prop={'size':8}, loc='best')
title(task_description + 'Proportion of vanilla Ruby performance by execution target', fontsize=8)
savefig(task_directory + '/prop_van.pdf', bbox_inches='tight')
show()

if show_bespoke:
    # percentage of bespoke performance
    vanilla_bp_laptop = [ b / x for (b, x) in zip(bespoke_ruby_laptop, vanilla_ruby_laptop)]
    cpu_bp_laptop = [ b / x for (b, x) in zip(bespoke_ruby_laptop, rubicl_cpu_laptop)]
    gpu_bp_laptop = [ b / x for (b, x) in zip(bespoke_ruby_laptop, rubicl_gpu_laptop)]

    vanilla_bp_pc = [ b / x for (b, x) in zip(bespoke_ruby_pc, vanilla_ruby_pc)]
    cpu_bp_pc = [ b / x for (b, x) in zip(bespoke_ruby_pc, rubicl_cpu_pc)]
    gpu_bp_pc = [ b / x for (b, x) in zip(bespoke_ruby_pc, rubicl_gpu_pc)]

    plot(input_sizes, vanilla_bp_laptop, linestyle='-', marker='o', markersize=4, color='r',
            label="Vanilla Ruby (Laptop)")
    plot(input_sizes, cpu_bp_laptop, linestyle='-', marker='o', markersize=4, color='b',
            label="RubiCL on CPU (Laptop)")
    plot(input_sizes, gpu_bp_laptop, linestyle='-', marker='o', markersize=4, color='g',
            label="RubiCL on GPU (Laptop)")

    plot(input_sizes, vanilla_bp_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='r',
            label="Vanilla Ruby (PC)")
    plot(input_sizes, cpu_bp_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='b',
            label="RubiCL on CPU (PC)")
    plot(input_sizes, gpu_bp_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='g',
            label="RubiCL on GPU (PC)")

    xlabel('Dataset size (elements)', fontsize=8)
    ylabel('Proportion of bespoke C extension performance', fontsize=8)
    legend(framealpha=0.2, prop={'size':8}, loc='best')
    title(task_description + 'Proportion of bespoke C extension performance by execution target', fontsize=8)
    savefig(task_directory + '/prop_bes.pdf', bbox_inches='tight')
    show()

# Time per element
vanilla_pe_laptop = [t / e for (t, e) in zip(vanilla_ruby_laptop, input_sizes)]
cpu_pe_laptop = [t / e for (t, e) in zip(rubicl_cpu_laptop, input_sizes)]
gpu_pe_laptop = [t / e for (t, e) in zip(rubicl_gpu_laptop, input_sizes)]

if show_bespoke:
    bespoke_pe_laptop = [t / e for (t, e) in zip(bespoke_ruby_laptop, input_sizes)]
    bespoke_pe_pc = [t / e for (t, e) in zip(bespoke_ruby_pc, input_sizes)]

vanilla_pe_pc = [t / e for (t, e) in zip(vanilla_ruby_pc, input_sizes)]
cpu_pe_pc = [t / e for (t, e) in zip(rubicl_cpu_pc, input_sizes)]
gpu_pe_pc = [t / e for (t, e) in zip(rubicl_gpu_pc, input_sizes)]

plot(input_sizes, vanilla_pe_laptop, linestyle='-', marker='o', markersize=4, color='r',
        label="Vanilla Ruby (Laptop)")
plot(input_sizes, cpu_pe_laptop, linestyle='-', marker='o', markersize=4, color='b',
        label="RubiCL on CPU (Laptop)")
plot(input_sizes, gpu_pe_laptop, linestyle='-', marker='o', markersize=4, color='g',
        label="RubiCL on GPU (Laptop)")

if show_bespoke:
    plot(input_sizes, bespoke_pe_laptop, linestyle='-', marker='o', markersize=4, color='k',
            label="Bespoke C Extension (Laptop)")
    plot(input_sizes, bespoke_pe_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='k',
            label="Bespoke C Extension (PC)")

plot(input_sizes, vanilla_pe_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='r',
        label="Vanilla Ruby (PC)")
plot(input_sizes, cpu_pe_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='b',
        label="RubiCL on CPU (PC)")
plot(input_sizes, gpu_pe_pc, linestyle='--', marker='o', markersize=4, fillstyle='left', color='g',
        label="RubiCL on GPU (PC)")

xlabel('Dataset size (elements)', fontsize=8)
ylabel('Runtime per element (seconds)', fontsize=8)
legend(framealpha=0.2, prop={'size':8}, loc='best')
title(task_description + 'Duration per element by execution target', fontsize=8)
savefig(task_directory + '/per_element.pdf', bbox_inches='tight')
show()

