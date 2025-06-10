import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

function UploadPage() {
  const onDrop = useCallback(acceptedFiles => {
    const file = acceptedFiles[0];
    const formData = new FormData();
    formData.append('file', file);

    axios.post('/api/upload', formData)
      .then(res => {
        console.log('Upload Success:', res.data);
      })
      .catch(err => {
        console.error('Upload Error:', err);
      });
  }, []);

  const { getRootProps, getInputProps } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} style={{ border: '2px dashed gray', padding: '20px', margin: '20px' }}>
      <input {...getInputProps()} />
      <p>Drag and drop sales data CSV here, or click to select</p>
    </div>
  );
}

export default UploadPage;
