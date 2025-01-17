import os
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":
    all_files = os.listdir('./')
    context_switch_fork = [] #subarray1 for mean, 2 for variance, 3 for std dev
    context_switch_kernel_thread = []
    measurement_overhead = []
    loop_overhead = []
    measurement_results = []
    memory_read_bw = [] #mean and std_dev is Gb/s
    memory_write_bw = []
    procedure_call_overhead = []
    ram_time = []
    ram_overhead = []
    system_call_overhead = []
    task_creation_fork_ovrhd = []
    task_creation_Kthread_ovrhd = []
    page_fault_ovrhd = []

    RAM = []
    for file in all_files:
        if(file == "measurement_overhead.txt"): #measurement_overhead.txt
            fp = open(file, "r")
            mean = []
            mean2 = []
            variance = []
            variance2 = []
            std_dev = []
            std_dev2 = []
            for line in fp:
                index_mean = line.find("Measurement Overhead(Mean)")
                if index_mean != -1:
                    string = line.split(":")
                    mean.append(float(string[1]))
                    
                index_variance = line.find("Measurement Overhead(Variance)")
                if index_variance != -1:
                    string = line.split(":")
                    variance.append(float(string[1]))
                    
                index_std_dev = line.find("Measurement Overhead(Mean)")
                if index_std_dev != -1:
                    string = line.split(":")
                    std_dev.append(float(string[1]))
                    
                index_mean2 = line.find("Loop Overhead(Mean)")
                if index_mean2 != -1:
                    string = line.split(":")
                    mean2.append(float(string[1]))
                    
                index_variance2 = line.find("Loop Overhead(Mean)")
                if index_variance2 != -1:
                    string = line.split(":")
                    variance2.append(float(string[1]))
                    
                index_std_dev2 = line.find("Loop Overhead(Mean)")
                if index_std_dev2 != -1:
                    string = line.split(":")
                    std_dev2.append(float(string[1]))
                    
            measurement_overhead.append(mean)
            measurement_overhead.append(variance)
            measurement_overhead.append(std_dev)
            loop_overhead.append(mean2)
            loop_overhead.append(variance2)
            loop_overhead.append(std_dev2)
        
        if(file == "memory_bandwidth_measurement.txt"):  # memory bandwidth.txt
            fp = open(file, "r")
            mean = []
            mean2 = []
            variance = []
            variance2 = []
            std_dev = []
            std_dev2 = []
            for line in fp:
                index_mean = line.find("Memory Read Bandwidth(Mean)")
                if index_mean != -1:
                    string = line.split(":")
                    mean.append(float(string[1]))

                index_variance = line.find("Memory Read Bandwidth(Variance)")
                if index_variance != -1:
                    string = line.split(":")
                    variance.append(float(string[1]))

                index_std_dev = line.find("Memory Read Bandwidth(Mean)")
                if index_std_dev != -1:
                    string = line.split(":")
                    std_dev.append(float(string[1]))

                index_mean2 = line.find("Memory Write Bandwidth(Mean)")
                if index_mean2 != -1:
                    string = line.split(":")
                    mean2.append(float(string[1]))

                index_variance2 = line.find("Memory Write Bandwidth(Mean)")
                if index_variance2 != -1:
                    string = line.split(":")
                    variance2.append(float(string[1]))

                index_std_dev2 = line.find("Memory Write Bandwidth(Mean)")
                if index_std_dev2 != -1:
                    string = line.split(":")
                    std_dev2.append(float(string[1]))

            memory_read_bw.append(mean)
            memory_read_bw.append(variance)
            memory_read_bw.append(std_dev)
            memory_write_bw.append(mean2)
            memory_write_bw.append(variance2)
            memory_write_bw.append(std_dev2)

        if(file == "procedure_call_measurement.txt"):  # procedure_call_overhead.txt
            fp = open(file, "r")
            mean = []
            mean2 = []
            variance = []
            for line in fp:
                index_mean = line.find("Procedure Call Overhead(Mean)")
                if index_mean != -1:
                    string = line.split(":")
                    mean.append(float(string[1]))

                index_variance = line.find("Procedure Call Overhead(Variance)")
                if index_variance != -1:
                    string = line.split(":")
                    variance.append(float(string[1]))

                index_std_dev = line.find("Procedure Call Overhead(Mean)")
                if index_std_dev != -1:
                    string = line.split(":")
                    std_dev.append(float(string[1]))
            procedure_call_overhead.append(mean)
            procedure_call_overhead.append(variance)
            procedure_call_overhead.append(std_dev)

        if(file == "ram_access_measurement.txt"):  # ram acccess measurements.txt
                fp = open(file, "r")
                mean = []
                mean2 = []
                variance = []
                for line in fp:
                    index_mean = line.find("RAM Access Overhead(Mean)")
                    if index_mean != -1:
                        string = line.split(":")
                        mean.append(float(string[1]))

                    index_variance = line.find("RAM Access Overhead(Variance)")
                    if index_variance != -1:
                        string = line.split(":")
                        variance.append(float(string[1]))

                    index_std_dev = line.find("RAM Access Overhead(Mean)")
                    if index_std_dev != -1:
                        string = line.split(":")
                        std_dev.append(float(string[1]))



                ram_overhead.append(mean)
                ram_overhead.append(variance)
                ram_overhead.append(std_dev)

        if(file == "system_call_measurement.txt"):  # system call measurements.txt
            fp = open(file, "r")
            mean = []
            mean2 = []
            variance = []
            for line in fp:
                index_mean = line.find("System Call Overhead(Mean)")
                if index_mean != -1:
                    string = line.split(":")
                    mean.append(float(string[1]))

                index_variance = line.find("System Call Overhead(Variance)")
                if index_variance != -1:
                    string = line.split(":")
                    variance.append(float(string[1]))

                index_std_dev = line.find("System Call Overhead(Mean)")
                if index_std_dev != -1:
                    string = line.split(":")
                    std_dev.append(float(string[1]))

            system_call_overhead.append(mean)
            system_call_overhead.append(variance)
            system_call_overhead.append(std_dev)

        if(file == "task_creation_measurement.txt"):  # task_creation_measurement.txt
            fp = open(file, "r")
            mean = []
            mean2 = []
            variance = []
            variance2 = []
            std_dev = []
            std_dev2 = []
            for line in fp:
                index_mean = line.find("Fork Overhead(Mean)")
                if index_mean != -1:
                    string = line.split(":")
                    mean.append(float(string[1]))

                index_variance = line.find("Fork Overhead(Variance)")
                if index_variance != -1:
                    string = line.split(":")
                    variance.append(float(string[1]))

                index_std_dev = line.find("Fork Overhead(Mean)")
                if index_std_dev != -1:
                    string = line.split(":")
                    std_dev.append(float(string[1]))

                index_mean2 = line.find("Kernel Thread Overhead(Mean)")
                if index_mean2 != -1:
                    string = line.split(":")
                    mean2.append(float(string[1]))

                index_variance2 = line.find("Kernel Thread Overhead(Mean)")
                if index_variance2 != -1:
                    string = line.split(":")
                    variance2.append(float(string[1]))

                index_std_dev2 = line.find("Kernel Thread Overhead(Mean)")
                if index_std_dev2 != -1:
                    string = line.split(":")
                    std_dev2.append(float(string[1]))

            task_creation_fork_ovrhd.append(mean)
            task_creation_fork_ovrhd.append(variance)
            task_creation_fork_ovrhd.append(std_dev)
            task_creation_Kthread_ovrhd.append(mean2)
            task_creation_Kthread_ovrhd.append(variance2)
            task_creation_Kthread_ovrhd.append(std_dev2)

        if(file == "context_switch_measurement.txt"):  # memory bandwidth.txt
            fp = open(file, "r")
            mean = []
            mean2 = []
            variance = []
            variance2 = []
            std_dev = []
            std_dev2 = []
            for line in fp:
                index_mean = line.find("Context Switch Fork Overhead(Mean)")
                if index_mean != -1:
                    string = line.split(":")
                    mean.append(float(string[1]))

                index_variance = line.find("Context Switch Fork Overhead(Variance)")
                if index_variance != -1:
                    string = line.split(":")
                    variance.append(float(string[1]))

                index_std_dev = line.find("Context Switch Fork Overhead(Mean)")
                if index_std_dev != -1:
                    string = line.split(":")
                    std_dev.append(float(string[1]))

                index_mean2 = line.find("Context Switch Fork Overhead(Mean)")
                if index_mean2 != -1:
                    string = line.split(":")
                    mean2.append(float(string[1]))

                index_variance2 = line.find("Context Switch Fork Overhead(Mean)")
                if index_variance2 != -1:
                    string = line.split(":")
                    variance2.append(float(string[1]))

                index_std_dev2 = line.find("Context Switch Fork Overhead(Mean)")
                if index_std_dev2 != -1:
                    string = line.split(":")
                    std_dev2.append(float(string[1]))

            context_switch_fork.append(mean)
            context_switch_fork.append(variance)
            context_switch_fork.append(std_dev)
            context_switch_kernel_thread.append(mean2)
            context_switch_kernel_thread.append(variance2)
            context_switch_kernel_thread.append(std_dev2)

        if(file == "page_fault_overhead.txt"):  # system call measurements.txt
                fp = open(file, "r")
                mean = []
                mean2 = []
                variance = []
                for line in fp:
                    index_mean = line.find("Page Fault Overhead(Mean)")
                    if index_mean != -1:
                        string = line.split(":")
                        mean.append(float(string[1]))

                    index_variance = line.find("Page Fault Overhead(Variance)")
                    if index_variance != -1:
                        string = line.split(":")
                        variance.append(float(string[1]))

                    index_std_dev = line.find("Page Fault Overhead(Mean)")
                    if index_std_dev != -1:
                        string = line.split(":")
                        std_dev.append(float(string[1]))

                page_fault_ovrhd.append(mean)
                page_fault_ovrhd.append(variance)
                page_fault_ovrhd.append(std_dev)
    # print( "measurement overhead: ", measurement_overhead,"\n", "loop overhead: ", loop_overhead ,'\n')
    # print( "memory read overhead: ", memory_read_bw,"\n", "memory write overhead: ", memory_write_bw, '\n')
    # print("proc call overhead: " , procedure_call_overhead, '\n')
    print("ram access: ", ram_overhead)
    def normalize( input):
        output = []
        mx = max(input)
        mn = min(input)
        for i in input:
            output.append((i - mn)/(mx - mn))
        return output

    fig, axes = plt.subplots(nrows = 3, ncols = 4)
    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    #measurement_overhead_plot
    axes[0,0].bar(range(len(measurement_overhead[1])),(measurement_overhead[1]), width=.25)
    axes[0,1].bar(range(len(loop_overhead[1])),(loop_overhead[1]), width=.25)
    axes[0,2].bar(range(len(memory_read_bw[1])),(memory_read_bw[1]), width=.25)
    axes[0,3].bar(range(len(memory_write_bw[1])),(memory_write_bw[1]), width=.25)
    axes[1,0].bar(range(len(procedure_call_overhead[0])),(procedure_call_overhead[0]), width=.25)
    axes[1,1].bar(range(len(ram_overhead[0])),(ram_overhead[0]), width=.25)
    axes[1,2].bar(range(len(system_call_overhead[0])),(system_call_overhead[0]), width=.25)
    axes[1,3].bar(range(len(task_creation_fork_ovrhd[0])),(task_creation_fork_ovrhd[0]), width=.25)
    axes[2,0].bar(range(len(task_creation_Kthread_ovrhd[0])),(task_creation_Kthread_ovrhd[0]), width=.25)
    axes[2,1].bar(range(len(context_switch_fork[0])),(context_switch_fork[0]), width=.25)
    axes[2,2].bar(range(len(context_switch_kernel_thread[0])),(context_switch_kernel_thread[0]), width=.25)
    axes[2, 3].bar(range(len(page_fault_ovrhd[0])),(page_fault_ovrhd[0]), width=.25)

    axes[0,0].set_title('measurement overhead')
    axes[0,1].set_title('loop overhead')
    axes[0,2].set_title('memory read bandwidth')
    axes[0,3].set_title('memory write bandwidth')
    axes[1,0].set_title('procedure call overhead')
    axes[1,1].set_title('RAM access overhead')
    axes[1,2].set_title('system call overhead')
    axes[1,3].set_title('task creation fork overhead')
    axes[2,0].set_title('task creation Kthread overhead')
    axes[2,1].set_title('contect switch fork overhead')
    axes[2,2].set_title('context switch kthread overhead')
    axes[2, 3].set_title('page fault overhead')


    plt.subplots_adjust(left=0.05, bottom=0.04, right=0.98,
                        top=0.94, wspace=0.21, hspace=0.22)
    plt.show()



    # fp = open(all_files[0], "r")
    # storage = []
    # for line in fp:
    #     index = line.find("Context Switch Fork Overhead(Mean)")
    #     if index != -1:
    #         string = line.split(":")
    #         storage.append(float(string[1]))
    # plt.bar(range(len(storage)), storage, width=.25)
    # plt.show()



    # print(storage)

