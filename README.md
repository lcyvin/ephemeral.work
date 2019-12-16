# Ephemeral.work is like twitter but worse
## (Or maybe better, depending on your definition of better)

---

What Ephemeral is:
- A conceptual social-networking webservice designed to explore how users interact with content in a limited scope
- A neat little project
- Something to keep me busy

What Ephemeral is not:
- A full-featured, comprehensive social media experience

## Design Philosophy
Ephemeral intends to deliver a lo-fi, simple-to-use platform which challenges how users consume and interact with other users' content when that content is short-lived (hence the name). A user can only ever have one post live on their account. When a new post is created, the old post is lost forever (audit logs not withstanding). It intends to create an experience which limits the amount of content one is capable of consuming at a given time, to determine if such an experience reduces the overwhelming aspect of more traditional social media services.

Ephemeral is not a business model, nor is it a product per se. It is an experiment and a statement. How do you use the platforms you are given, and what is the message that users consuming your content come away with? How can a user on a site with such limitations make use of the platform in a way they find engaging and fulfilling? 

## Design Practicalities
Ephemeral is written in python3 using the Flask microframework, with SQLAlchemy backend for data integration. It is not designed with massive scalability in mind, and should that become a need, future design considerations will need to be made to accomodate. 

## Contributing
Ephemeral is FOSS and as such open to forking, modification, and contribution from willing parties. Our contribution guidelines can be read [here](contributions.md)

# Installation for Development
Ephemeral can be installed on your development machine by simply cloning the repo and installing python's requirements from the requirements.txt file. It is recommended that you use [virtualenv](https://github.com/pypa/virtualenv) for development.

## License
Ephemeral is licensed under an [MIT License](LICENSE)
