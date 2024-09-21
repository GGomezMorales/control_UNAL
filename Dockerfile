FROM continuumio/miniconda3

RUN conda install jupyter jupyterlab ipykernel -y \
    && conda install -c conda-forge nb_conda_kernels -y \
    && conda install -c conda-forge control slycot -y \
    && conda install conda-forge::prettytable -y

RUN jupyter-lab --generate-config

COPY ./.config/jupyter_lab_config.py /root/.jupyter/jupyter_lab_config.py

CMD ["jupyter-lab", "./control/lessons", "--allow-root"]
