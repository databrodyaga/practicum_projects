# Prediction of Alloy Temperature for the MK "Steel Bird"

## Project Description

To optimize production costs, the metallurgical plant "Steel Bird" decided to reduce electricity consumption during the steel processing stage. To achieve this, the plant needs to control the alloy temperature. Our task is to **build a model** that will predict this temperature.  
The customer wants to use the developed model to simulate the technological process. Below we provide the details of the tech process.

### Description of the Processing Stage
Steel is processed in a metal ladle with a capacity of about 100 tons. To withstand high temperatures, the ladle is lined inside with refractory bricks. Molten steel is poured into the ladle and heated to the desired temperature using graphite electrodes installed in the ladle's lid.  
Sulfur is removed from the alloy (this process is called desulfurization), the chemical composition is adjusted by adding impurities, and samples are taken. Steel is alloyed—its composition is modified—by feeding alloy chunks from a bulk material bunker or wire through a special trib-apparatus (from the English "tribe," meaning "mass").  
Before the first alloying additives are introduced, the steel temperature is measured, and its chemical analysis is conducted. Then, the temperature is raised for a few minutes, alloying materials are added, and the alloy is blown with an inert gas. Afterward, it is mixed, and the measurements are repeated. This cycle is repeated until the target chemical composition and optimal melting temperature are reached.  
At that point, the molten steel is either sent for metal finishing or fed into the continuous casting machine. From there, the final product emerges in the form of slabs (from the English "slab," meaning "plate").

## Data Description

The data consists of several files obtained from different sources:  
- data_arc_new.csv — electrode data;
- data_bulk_new.csv — bulk material feed data (volume);
- data_bulk_time_new.csv — bulk material feed data (time);
- data_gas_new.csv — alloy gas blowing data;
- data_temp_new.csv — temperature measurement results;
- data_wire_new.csv — wire material data (volume);
- data_wire_time_new.csv — wire material data (time).

### data_arc_new.csv:  
- key — batch number;
- Начало нагрева дугой — heating start time;
- Конец нагрева дугой  — heating end time;
- Активная мощность — active power value;
- Реактивная мощность — reactive power value.

### data_bulk_new.csv:
- key — batch number;
- Bulk 1 … Bulk 15 — volume of the supplied material.

### data_bulk_time_new.csv: 
- key — batch number;
- Bulk 1 … Bulk 15 — material feed time.

### data_gas_new.csv:
- key — batch number;
- Газ 1 — volume of the supplied gas.

### data_temp_new.csv:
- key — batch number;
- Время замера — measurement time;
- Температура — temperature value.

### data_wire_new.csv:
- key — batch number;
- Wire 1 … Wire 9 — volume of the supplied wire materials.

### data_wire_time_new.csv:  
- key — batch number;
- Wire 1 … Wire 9 — wire material feed time.

In all files, the `key` column contains the batch number. Files may have several rows with the same `key` value, corresponding to different iterations of processing.

Specific steps for data analysis and prediction are detailed throughout the notebook.

In this **Final Project**, many stages previously worked on were implemented:  
- refining the task with the customer,
- conducting all stages of data analysis and machine learning,
- implementing the project as close as possible to real-world work.