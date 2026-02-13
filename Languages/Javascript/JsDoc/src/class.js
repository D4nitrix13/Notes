// Author: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Email: danielperezdev@proton.me

/**
 * Class to create a Programmer
 */
class Programmer {
  /**
   * Create a new Programmer
   * @param {Object} user User's information
   * @param {string} user.fullname Programmer's full name
   * @param {string} language A programming language name
   */
  constructor(user, language) {
    /**
     * @property {string} fullname Programmer's full name
     */
    this.fullname = user.fullname;

    /**
     * @property {string} language The programmer's programming language
     */
    this.language = language;
  }

  /**
   * Get the programmer's information
   * @returns {void}
   */
  getInfo() {
    console.log(
      `I'm ${this.fullname} and my favorite programming language is ${this.language}`
    );
  }
}

/**
 * Example usage:
 * @example
 * const newProgrammer = new Programmer({ fullname: "Ryan Ray" }, "golang");
 * newProgrammer.getInfo();
 */

/**
 * GitHub Library
 * @example
 * const github = new Github({
 *   username: 'D4nitrix13',
 *   token: 'xyz123'
 * });
 * const repositories = github.getRepositories();
 *
 * @see https://docs.github.com/es/rest/repos
 * @todo Implement the remaining methods
 */
class Github {
  /**
   * Create a new Github instance
   * @param {Object} options Configuration options
   * @param {string} options.user GitHub username
   * @param {string} options.token GitHub secret token
   */
  constructor({ user, token }) {
    this.user = user;
    this.token = token;
  }

  /**
   * List all public repositories for the user
   * @param {Object} options Configuration options
   * @param {number} [options.limit=6] The limit of repositories to return
   * @returns {Array<Object>} An array of public repositories
   */
  getRepositories({ limit = 6 }) {
    return [];
  }
}
