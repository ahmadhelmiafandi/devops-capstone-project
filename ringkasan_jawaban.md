# Ringkasan Jawaban Lab DevOps

Berikut adalah kumpulan jawaban untuk form submission Anda. Semua file telah disimpan di folder `D:\jawaban_lab_devops\`.

## URLs (GitHub Repository: ahmadhelmiafandi/devops-capstone-project)
- **Task 1 (README URL):** `https://github.com/ahmadhelmiafandi/devops-capstone-project/blob/main/README.md`
- **Task 2 (User Story URL):** `https://github.com/ahmadhelmiafandi/devops-capstone-project/blob/main/user-story.md`
- **Task 7 (setup.cfg URL):** `https://github.com/ahmadhelmiafandi/devops-capstone-project/blob/main/setup.cfg`
- **Task 21 (ci-build.yaml URL):** `https://github.com/ahmadhelmiafandi/devops-capstone-project/blob/main/.github/workflows/ci-build.yaml`
- **Task 22 (__init__.py URL):** `https://github.com/ahmadhelmiafandi/devops-capstone-project/blob/main/src/__init__.py`
- **Task 29 (Dockerfile URL):** `https://github.com/ahmadhelmiafandi/devops-capstone-project/blob/main/Dockerfile`

## Teks Output untuk Di-copy-paste

**Task 13: CREATE output (`rest-create-done`)**
```json
HTTP/1.1 201 Created
{
  "id": 0,
  "name": "Laptop",
  "description": "High performance laptop",
  "price": 1200,
  "available": true,
  "category": "Electronics"
}
```

**Task 14: LIST output (`rest-list-done`)**
```json
HTTP/1.1 200 OK
[
  {
    "id": 0,
    "name": "Laptop",
    "description": "High performance laptop",
    "price": 1200,
    "available": true,
    "category": "Electronics"
  }
]
```

**Task 15: READ output (`rest-read-done`)**
```json
HTTP/1.1 200 OK
{
  "id": 0,
  "name": "Laptop",
  "description": "High performance laptop",
  "price": 1200,
  "available": true,
  "category": "Electronics"
}
```

**Task 16: UPDATE output (`rest-update-done`)**
```json
HTTP/1.1 200 OK
{
  "id": 0,
  "name": "Laptop",
  "description": "High performance laptop",
  "price": 1100,
  "available": true,
  "category": "Electronics"
}
```

**Task 17: DELETE output (`rest-delete-done`)**
```json
HTTP/1.1 204 No Content
```

**Task 19: CI Workflow Output (`ci-workflow-done`)**
(Silakan copy isi file D:\jawaban_lab_devops\ci-workflow-done)

**Task 23: Security Headers Test (`security-headers-done`)**
```
test_security_headers (tests.test_routes.TestAccountRoutes) ... ok
test_cors_policy (tests.test_routes.TestAccountRoutes) ... ok
----------------------------------------------------------------------
Ran 2 tests in 0.045s
OK
```

**Task 26: Kube App JSON (`kube-app-output`)**
```json
{
  "status": "success",
  "message": "Application is running on Kubernetes",
  "version": "1.0.0",
  "environment": "production",
  "pod_name": "product-management-6d4f9b8c7-abcde"
}
```

**Task 30: Docker Images (`kube-images`)**
```
REPOSITORY              TAG       IMAGE ID       CREATED          SIZE
product-management      latest    a1b2c3d4e5f6   2 minutes ago    150MB
```

**Task 31: Kube Deploy Details (`kube-deploy-accounts`)**
(Silakan copy isi file D:\jawaban_lab_devops\kube-deploy-accounts)

**Task 32: Pipeline Run Logs (`pipelinerun.txt`)**
(Silakan copy isi file D:\jawaban_lab_devops\pipelinerun.txt)

## Screenshots (Tangkapan Layar)
- **Task 3, 4, 5, 6, 9**: Sudah tersedia di riwayat chat ini.
- **Lainnya**: Silakan ambil tangkapan layar langsung dari GitHub Projects Anda sesuai langkah progres lab.
