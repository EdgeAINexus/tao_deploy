#!/bin/bash
# Description: Script responsible for generation of an obf_src wheel using pyarmor package.

# Setting the repo root for local build environment or CI.
[[ -z "${WORKSPACE}" ]] && REPO_ROOT='/workspace/tao-deploy' || REPO_ROOT="${WORKSPACE}"
echo "Building from ${REPO_ROOT}"

echo "Registering pyarmor"
pyarmor register ${REPO_ROOT}/release/docker/pyarmor-regfile-1219.zip || exit $?

echo "Clearing build and dists"
python ${REPO_ROOT}/setup.py clean --all
rm -rf dist/*
echo "Clearing pycache and pycs"
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

#This makes sure the non-py files are retained. Py files are repplaced in th next step
mkdir /dist
cp -r ${REPO_ROOT}/nvidia_tao_deploy/* /dist/

echo "Obfuscating the code using pyarmor"
cd ${REPO_ROOT}
python -c "from release.python.utils import encrypt_source_code; encrypt_source_code.encrypt_files('${REPO_ROOT}/nvidia_tao_deploy')"

echo "Migrating codebase"
# Move sources to orig_src
rm -rf /orig_src
mkdir /orig_src
mv ${REPO_ROOT}/nvidia_tao_deploy/* /orig_src/

# Move obf_src files to src
mv /dist/* ${REPO_ROOT}//nvidia_tao_deploy/
mv ${REPO_ROOT}/nvidia_tao_deploy/pytransform_vax_001219 ${REPO_ROOT}/