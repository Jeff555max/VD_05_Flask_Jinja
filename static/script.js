document.addEventListener('DOMContentLoaded', () => {
  const blogPosts = document.querySelectorAll('.blog-post');

  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);

  blogPosts.forEach(post => {
    post.style.opacity = '0';
    post.style.transform = 'translateY(20px)';
    post.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    observer.observe(post);
  });
});