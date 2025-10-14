// firebase.js
// بارگذاری Firebase از CDN (برای مرورگر)
const firebaseConfig = {
  apiKey: "AIzaSyDFxoFm-JYmXeFmqBNyJhl5XKhZ7GPqEM0",
  authDomain: "panel-3159b.firebaseapp.com",
  projectId: "panel-3159b",
  storageBucket: "panel-3159b.firebasestorage.app",
  messagingSenderId: "955867957315",
  appId: "1:955867957315:web:1a49b15346364587326cf6",
  measurementId: "G-S1RZEZZL15"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
