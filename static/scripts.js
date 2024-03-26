document.addEventListener('DOMContentLoaded', function () {
    const cameraBtn = document.getElementById('camera');
    const videoInput = document.getElementById('video');
    const imageInput = document.getElementById('image');
    const previewDiv = document.getElementById('preview');
    const cameraStream = document.getElementById('cameraStream');

    cameraBtn.addEventListener('click', function () {
        // Mở camera ở đây (có thể sử dụng API getUserMedia hoặc thư viện như Webcam.js)
        // Để đơn giản, ta chỉ hiển thị một hình ảnh tĩnh nếu không thể mở camera.
        cameraStream.innerHTML = '<img src="static/static-image.jpg" alt="Camera Image">';
    });

    videoInput.addEventListener('change', function () {
        const file = this.files[0];
        // Hiển thị video tại đây (có thể sử dụng thư viện như Plyr hoặc Video.js)
        previewDiv.innerHTML = `<p>Selected Video: ${file.name}</p>`;
    });

    imageInput.addEventListener('change', function () {
        const file = this.files[0];
        // Hiển thị hình ảnh tại đây
        previewDiv.innerHTML = `<p>Selected Image: ${file.name}</p>`;
    });
});
