{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "82696748-3025-48b7-8f6e-50f911185af8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def savings(gross_pay,tax_rate,expenses):\n",
    "    savings=int(gross_pay*(1-tax_rate))-expenses\n",
    "    return savings\n",
    "def material_waste(total_material,material_units,num_jobs,job_consumption):\n",
    "    material_waste=total_material-(num_jobs*job_consumption)\n",
    "    final_answer=str(str(material_waste)+material_units)\n",
    "    return final_answer\n",
    "def interest(principal, rate, periods):\n",
    "    interest=int(principal+(principal*rate*periods))\n",
    "    return interest\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfeb9c22-2444-43d8-adec-890aab049b4f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
